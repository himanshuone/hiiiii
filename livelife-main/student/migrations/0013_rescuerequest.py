# Generated by Django 5.0.4 on 2024-05-13 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='RescueRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('', 'Select Category'), ('disabled', 'Disabled'), ('wounded', 'Wounded'), ('orphan', 'Orphan')], default='', max_length=20)),
                ('location', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
