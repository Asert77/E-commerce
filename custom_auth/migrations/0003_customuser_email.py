# Generated by Django 5.1.5 on 2025-03-24 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0002_alter_customuser_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=254, unique=True),
        ),
    ]
