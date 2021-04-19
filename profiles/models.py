from django.db import models
from accounts.models import MyUser


class Profile(models.Model):
    owner = models.OneToOneField(MyUser, primary_key=True, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_image')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_number = models.PositiveIntegerField()
    citizenship_number = models.PositiveIntegerField()
    citizenship_front = models.ImageField(upload_to='citizenship')
    citizenship_back = models.ImageField(upload_to='citizenship')
    temp_address = models.CharField(max_length=50)
    per_address = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)