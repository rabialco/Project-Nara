# Generated by Django 2.2.5 on 2019-12-06 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0004_auto_20191206_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='thumb',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='nama',
            field=models.CharField(default='Fill here!', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='Fill here!', max_length=30),
        ),
    ]
