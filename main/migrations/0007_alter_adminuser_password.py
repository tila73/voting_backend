# Generated by Django 4.1.7 on 2023-03-10 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_adminuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$oP78YfN0FXyOMatgd7orP2$qRZHUOaDlc7fjAMMqBiiU+86/HCB8QX348E/K0Fgqw0=', max_length=128, verbose_name='Password'),
        ),
    ]
