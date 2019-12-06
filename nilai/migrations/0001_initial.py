# Generated by Django 2.2.5 on 2019-12-06 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mata_kuliah', models.CharField(max_length=30)),
                ('sks', models.IntegerField(default=0)),
                ('nilai', models.FloatField(choices=[(4.0, 'A'), (3.7, 'A-'), (3.3, 'B+'), (3.0, 'B'), (2.7, 'B-'), (2.3, 'C+'), (2.0, 'C'), (1.0, 'D'), (0.0, 'E')])),
                ('semester', models.IntegerField(default=0)),
            ],
        ),
    ]