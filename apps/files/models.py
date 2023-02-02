from pathlib import Path
from time import strftime, localtime

from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import Patient

import uuid


def file_path(instance, filename):
    return '{0}/{1}{2}'.format(strftime('%Y/%m/%d', localtime()), uuid.uuid4(), Path(filename).suffix)


class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False, upload_to=file_path)
    file_name = models.TextField()

    def __str__(self):
        return self.file_name


# Patient Attachements

class Attachment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name='attachments')
    file = models.ForeignKey(
        File, on_delete=models.CASCADE, related_name='attachments')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.file.file_name
