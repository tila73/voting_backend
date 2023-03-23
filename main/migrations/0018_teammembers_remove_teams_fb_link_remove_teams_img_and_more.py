# Generated by Django 4.1 on 2023-03-19 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_testimonial_testimonial_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/teams')),
                ('name', models.CharField(max_length=60)),
                ('post', models.CharField(max_length=100)),
                ('fb_link', models.CharField(max_length=150)),
                ('twitter_link', models.CharField(max_length=150)),
                ('insta_link', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=True, help_text='0=inactive, 1=active')),
            ],
        ),
        migrations.RemoveField(
            model_name='teams',
            name='fb_link',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='img',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='insta_link',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='post',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='status',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='twitter_link',
        ),
    ]