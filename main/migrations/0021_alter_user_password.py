# Generated by Django 4.1.7 on 2023-03-19 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_merge_20230319_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, verbose_name='Password'),
        ),
    ]
