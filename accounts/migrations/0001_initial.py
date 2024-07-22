# Generated by Django 5.0.6 on 2024-06-03 17:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255, verbose_name='نام')),
                ('last_name', models.CharField(max_length=255, verbose_name='نام خانوادگی')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='لطفا یک شماره همراه معتبر وارد کنید.', regex='^[0][9]\\d{9}$')], verbose_name='شماره تلفن')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='مدیر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('is_verified', models.BooleanField(default=False, verbose_name='تایید شده / نشده')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ عضویت')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='تاریخ بروزرسانی')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها',
            },
        ),
    ]