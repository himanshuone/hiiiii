# Generated by Django 5.0.4 on 2024-05-13 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0011_sponsor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, upload_to='services/')),
            ],
        ),
    ]
