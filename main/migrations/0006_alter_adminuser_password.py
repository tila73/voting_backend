# Generated by Django 4.1.7 on 2023-03-10 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_adminuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='', max_length=128, verbose_name='Password'),
        ),
    ]
