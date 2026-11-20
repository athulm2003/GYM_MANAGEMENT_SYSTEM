from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class MemberShipDb(models.Model):
    member=models.ForeignKey(User,on_delete=models.CASCADE,related_name="memberships")
    plan_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    amount=models.IntegerField()
    start_date=models.DateField()
    end_date=models.DateField()
    status=models.CharField(max_length=50,default="Active")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name
