# Generated by Django 2.2.6 on 2019-10-31 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescuemap', '0002_auto_20191031_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='victim',
            name='address',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
