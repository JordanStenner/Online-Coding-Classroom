# Generated by Django 3.0.5 on 2020-11-09 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('classroom_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('role', models.CharField(choices=[('TEACHER', 'Teacher'), ('STUDENT', 'Student'), ('AVERAGE', 'Average User')], max_length=12)),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=30)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('classNum', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='classroom_main.ComputingClass')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
