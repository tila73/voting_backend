# Generated by Django 4.1.5 on 2023-03-20 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_faq_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='status',
        ),
    ]
