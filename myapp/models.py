from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)  # For simplicity; use better password storage in practice
    image = models.ImageField(upload_to='user_profile_images/',default='path/to/default/image.png')
    preserve_default=False,



