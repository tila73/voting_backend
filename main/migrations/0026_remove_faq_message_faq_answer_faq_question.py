# Generated by Django 4.1.5 on 2023-03-21 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_merge_0020_merge_20230319_1642_0024_remove_faq_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='message',
        ),
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question',
            field=models.TextField(null=True),
        ),
    ]
