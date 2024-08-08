from django.db import models

class UploadedFile(models.Model):
    file = models.FileField(upload_to='files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class VoiceRecording(models.Model):
    voice = models.FileField(upload_to='voices/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
