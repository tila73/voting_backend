# Generated by Django 4.1.7 on 2023-03-19 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='status',
        ),
    ]
