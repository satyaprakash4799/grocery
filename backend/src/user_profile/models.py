from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser

# class User(AbstractBaseUser):
    # pass
class UserProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile', primary_key=True)
    age = models.IntegerField(default=18, null=False, blank=False)
    phone_number = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = "user profiles"

class Addresses(models.Model):
    """
    User addresses model
    """
    user_profile = models.ForeignKey(UserProfiles, on_delete=models.CASCADE, related_name='addresses')
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
        verbose_name_plural = "User addresses"

class BlackListedToken(models.Model):
    """
    List of blacklisted tokens that are not allowed
    """
    token = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='token_user', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('token', 'user')