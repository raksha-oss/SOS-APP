# Generated by Django 2.2.6 on 2019-11-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rescuemap', '0007_auto_20191105_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rescueteam',
            name='profession',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='situation',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
