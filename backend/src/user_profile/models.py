from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfiles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(default=18, null=False, blank=False)
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

class Addresses(models.Model):
    """
    User addresses model
    """
    user_profile = models.ForeignKey(UserProfiles, on_delete=models.CASCADE)
    house_no = models.IntegerField(blank=False, null=False)
    apartment_name = models.CharField(max_length=255, null=True, blank=True)
    street_details = models.CharField(max_length=255, null=True, blank=True)
    landmark_details = models.CharField(max_length=255, null=True, blank=True)
    area_details = models.CharField(max_length=255, null=False, blank=False)
    city = models.CharField(max_length=255, null=False, blank=False)
    pincode = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.user_profile.user.username
    
    class Meta:
        verbose_name = "User address"
        verbose_name_plural = "User adresses"