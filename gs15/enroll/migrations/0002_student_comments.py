# Generated by Django 3.2.7 on 2021-11-16 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='comments',
            field=models.CharField(default='not available', max_length=70),
        ),
    ]
