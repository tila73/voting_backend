# Generated by Django 4.1.5 on 2023-03-15 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_adminuser_password_alter_eventdetails_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$44D184dRFZQWZ6qOAT4141$f3HOAaqqhPjVQmjgvVY8sKKK5kZlcjhG3+eeZWpuSpQ=', max_length=128, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_img',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
