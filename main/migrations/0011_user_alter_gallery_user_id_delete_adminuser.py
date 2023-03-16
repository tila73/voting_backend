# Generated by Django 4.1.7 on 2023-03-16 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_adminuser_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email')),
                ('password', models.CharField(default='pbkdf2_sha256$390000$NsmgtyE8AeoXM1QgiTUOh3$ca+Dqm/6fblJpXwJOu/O/wVe+IoZDWl1PIuP+xa6aiU=', max_length=128, verbose_name='Password')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='Address')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Phone Number')),
                ('esewa_number', models.CharField(max_length=100, null=True, verbose_name='Esewa Number')),
                ('role', models.IntegerField(default=1, help_text='0=business user(owner), 1=admin, 2=sub business user(owner)', verbose_name='User Role')),
                ('status', models.BooleanField(default=True, help_text='0=inactive, 1=active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
                ('updated_at', models.DateTimeField(verbose_name='Updated Date')),
            ],
        ),
        migrations.AlterField(
            model_name='gallery',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.DeleteModel(
            name='AdminUser',
        ),
    ]