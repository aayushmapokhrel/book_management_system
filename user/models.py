from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserBalance(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    balance = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.user.username