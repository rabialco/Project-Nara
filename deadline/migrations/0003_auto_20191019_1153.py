# Generated by Django 2.2.5 on 2019-10-19 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deadline', '0002_dl_selesai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dl',
            name='nama_deadline',
            field=models.CharField(blank=True, max_length=20, verbose_name=''),
        ),
    ]
