# Generated by Django 2.2.10 on 2020-03-12 17:41

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200311_0456'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=account.models.avatar_path),
        ),
    ]
