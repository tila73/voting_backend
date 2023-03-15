# Generated by Django 4.1.5 on 2023-03-15 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_adminuser_password_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$FvaKaeHu7FnH8NMMwtY9J2$Y9+yg2FWla23gt6Ep8PXK2vRo5I2Wtrq0kZtsy4EX8E=', max_length=128, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='eventdetails',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]
