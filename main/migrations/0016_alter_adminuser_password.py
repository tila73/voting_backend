# Generated by Django 4.1.7 on 2023-03-10 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_adminuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$YD1ccZVP2akFry3AecQAfA$Knrhsf9jYKnj1yCwfVCbGlXjs0JM2YFJh8hSr9M3NIA=', max_length=128, verbose_name='Password'),
        ),
    ]
