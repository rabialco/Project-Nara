# Generated by Django 2.2.5 on 2019-12-06 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_deadline', models.CharField(blank=True, max_length=25, verbose_name='')),
                ('selesai', models.BooleanField(default=False)),
            ],
        ),
    ]
