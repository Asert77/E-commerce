# Generated by Django 5.1.5 on 2025-03-26 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0011_alter_customuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, default='default@example.com', max_length=254, null=True),
        ),
    ]
