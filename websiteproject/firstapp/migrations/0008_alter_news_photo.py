# Generated by Django 4.0.1 on 2022-02-04 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_alter_news_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='photo',
            field=models.ImageField(default=' ', upload_to='photos/%Y/%m/%d'),
        ),
    ]
