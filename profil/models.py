from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    PILIHAN_SEMESTER = [
        (1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(-1,'Not a College Student')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    semester = models.DecimalField(choices=PILIHAN_SEMESTER, default=1, max_digits=1, decimal_places=0)
    motto = models.CharField(max_length=30, blank=True)