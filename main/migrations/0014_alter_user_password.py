# Generated by Django 4.1.7 on 2023-03-16 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$xMyLdakY4sdl0SIkmJ5kX4$Hq4TRO4XtEuys1AixhvuQ+cR7MNzxYC79tXUiLgGnPg=', max_length=128, verbose_name='Password'),
        ),
    ]
