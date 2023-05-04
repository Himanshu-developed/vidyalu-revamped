from django.db import models
from core.models.users import User

class  OtpVerification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    otp= models.IntegerField()
    is_verified=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    
