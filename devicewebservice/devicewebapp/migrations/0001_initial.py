# Generated by Django 3.2.7 on 2021-12-03 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_site', models.URLField(blank=True)),
                ('user_img', models.ImageField(blank=True, upload_to='user_imgs')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceProfileInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ndevice', models.CharField(max_length=128)),
                ('device_token', models.CharField(blank=True, max_length=256)),
                ('device_site', models.URLField(blank=True)),
                ('device_img', models.ImageField(blank=True, upload_to='device_imgs')),
                ('uowner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devicewebapp.userprofileinfo')),
            ],
        ),
    ]
