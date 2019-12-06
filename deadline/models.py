from django.db import models

# Create your models here.
class dl(models.Model):
    nama_deadline = models.CharField(max_length=25,blank=True, verbose_name='')
    selesai = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_deadline 