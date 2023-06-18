from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class notes(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notes_text = models.CharField(max_length=6000, blank=True)
    notes_file = models.FileField(blank=True, upload_to='notes/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class shared(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="createdby")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name="userid")
    note_id = models.ForeignKey('notes',verbose_name="note",on_delete=models.CASCADE)
