# Generated by Django 4.1.7 on 2023-03-10 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_adminuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$ARW2NKAGBk3Yt6eHkVffmS$3EI/XCVxaEwVas/+G+LVnJCnHCVCjJf2RytojKj7vHs=', max_length=128, verbose_name='Password'),
        ),
    ]