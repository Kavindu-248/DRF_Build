from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from django.db.models import Q

from apps.users.permissions import AnonWriteOnly, NotAllowed
from apps.users.serializers import AuthRegisterSerializer, UserSerializer, PasswordChangeSerializer, \
    ProfileUpdateSerializer, UserRequestResetPasswordSerializer, UserResetPasswordSerializer
from apps.users.models import User, Doctor, Patient, PharmacyUser
from apps.users.services import request_password_reset
from project import settings


class AuthViewSet(ViewSet):
    def get_permissions(self):
        if (self.action == 'register' and settings.SELF_REGISTER) or self.action == 'request_password_reset':
            permission_classes = [AnonWriteOnly]
        elif self.action == 'change_password':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [NotAllowed]
        return [permission() for permission in permission_classes]

    @action(methods=['post'], detail=False)
    def register(self, request):
        serializer = AuthRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['post'], detail=False, url_path='change-password')
    def change_password(self, request):
        serializer = PasswordChangeSerializer(
            data=request.data, instance=request.user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response()

    @action(methods=['post'], detail=False, url_path='request-password-reset')
    def request_password_reset(self, request):
        serializer = UserRequestResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                user = get_object_or_404(User, email=request.data['email'])
                request_password_reset(user)
            except Http404:
                pass
            finally:
                message = 'Password reset link has been sent to the registered email address.'
            return Response(message, status=status.HTTP_200_OK)

    @action(methods=['post'], detail=False, url_path='reset-password')
    def reset_password(self, request):
        serializer = UserResetPasswordSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.user
            user.set_password(serializer.validated_data.get('new_password'))
            user.save()
            return Response()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'me':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAuthenticated, IsAdminUser]

        return [permission() for permission in permission_classes]

    def register_doctor(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            doctor = serializer.save()
            user = User.objects.create(
                username=doctor.username, email=doctor.email)
            user.doctorprofile = doctor
            user.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=400)

    def register_patient(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            patient = serializer.save()
            user = User.objects.create(
                username=patient.username, email=patient.email)
            user.patientprofile = patient
            user.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=400)

    def register_pharmacy_user(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            pharmacy_user = serializer.save()
            user = User.objects.create(
                username=pharmacy_user.username, email=pharmacy_user.email)
            user.pharmacyuserprofile = pharmacy_user
            user.save()
            return Response(UserSerializer(user).data)
        return Response(serializer.errors, status=400)


class DoctorViewSet(ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = UserSerializer


class PatientViewSet(ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = UserSerializer


class PharmacyUserViewSet(ModelViewSet):
    queryset = PharmacyUser.objects.all()
    serializer_class = UserSerializer
