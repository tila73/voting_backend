# Generated by Django 4.1.5 on 2023-03-09 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=50, verbose_name='Title')),
                ('about_description', models.TextField(max_length=500, verbose_name='Description')),
                ('about_img', models.ImageField(upload_to='img/about/', verbose_name='Image')),
                ('status', models.BooleanField(default=True, help_text='0=inactive, 1=active')),
            ],
        ),
        migrations.CreateModel(
            name='Counts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count_number', models.PositiveIntegerField(verbose_name='Count Number')),
                ('count_title', models.CharField(max_length=50, verbose_name='Title')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_title', models.CharField(max_length=50, verbose_name='Title')),
                ('event_description', models.TextField(verbose_name='Description')),
                ('event_date', models.DateTimeField(verbose_name='Date')),
                ('event_img', models.ImageField(upload_to='img/event/', verbose_name='Image')),
                ('slug', models.SlugField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=50, verbose_name='Title')),
                ('news_description', models.TextField(verbose_name='Description')),
                ('news_author', models.CharField(max_length=50, verbose_name='Written By')),
                ('news_date', models.DateTimeField(verbose_name='News date')),
                ('news_img', models.ImageField(upload_to='img/news/', verbose_name='Image')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_title', models.CharField(max_length=50, verbose_name='Title')),
                ('slider_description', models.TextField(max_length=255, verbose_name='Description')),
                ('slider_img', models.ImageField(upload_to='img/slider/', verbose_name='Image')),
                ('status', models.BooleanField(default=True, help_text='0=inactive, 1=active')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testmoni_name', models.CharField(max_length=50, verbose_name='Name')),
                ('testmoni_designation', models.CharField(max_length=30, verbose_name='Designation')),
                ('testmoni_message', models.TextField(verbose_name='Message')),
                ('status', models.BooleanField(default=True, help_text='0=inactive, 1=active')),
            ],
        ),
    ]