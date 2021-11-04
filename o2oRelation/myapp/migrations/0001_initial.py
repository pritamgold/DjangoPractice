# Generated by Django 3.2.7 on 2021-09-28 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('page_name', models.CharField(max_length=25)),
                ('page_cat', models.CharField(max_length=20)),
                ('page_publish_date', models.DateField()),
            ],
        ),
    ]
