# Generated by Django 2.1.2 on 2018-11-02 09:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequestMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConnectedOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization_name', models.CharField(max_length=250)),
                ('logo', models.FileField(upload_to='')),
                ('web_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('facebook_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DonationProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('heading', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('position', models.CharField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_author', models.CharField(max_length=250)),
                ('image_title', models.CharField(max_length=250)),
                ('image', models.ImageField(default='gallery', upload_to='')),
                ('upload_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-upload_time'],
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='team_member_photo', upload_to='')),
                ('profile_name', models.CharField(max_length=250)),
                ('position', models.CharField(max_length=200)),
                ('facebook_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('instagram_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('twitter_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('googleplus_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('linkedin_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
                ('github_link', models.CharField(max_length=120, validators=[django.core.validators.URLValidator()])),
            ],
        ),
    ]
