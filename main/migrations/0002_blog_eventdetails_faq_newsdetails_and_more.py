# Generated by Django 4.1.5 on 2023-03-14 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='img/blogImg/')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('author_img', models.ImageField(upload_to='img/authorImg/')),
                ('slug', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='EventDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=100, verbose_name='Title')),
                ('event_description', models.TextField(verbose_name='Description')),
                ('event_date', models.DateTimeField(verbose_name='Date')),
                ('event_img', models.ImageField(upload_to='img/event/', verbose_name='Image')),
                ('slug', models.SlugField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('status', models.BooleanField(default=False, help_text='0=default, 1-Active')),
            ],
        ),
        migrations.CreateModel(
            name='NewsDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=5100, verbose_name='Title')),
                ('news_description', models.TextField(verbose_name='Description')),
                ('news_author', models.CharField(max_length=50, verbose_name='Written By')),
                ('news_date', models.DateTimeField(verbose_name='News date')),
                ('news_img', models.ImageField(upload_to='img/news/', verbose_name='Image')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='adminuser',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$390000$2CkmGneTxBRaf6bfOlbw9y$S8G4kmwIrC6J87CBVXtImCCiQhqW99+h/eZ/S0LNocQ=', max_length=128, verbose_name='Password'),
        ),
    ]