# Generated by Django 3.0.3 on 2020-02-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fe7', '0005_character_base_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='recruitment_chapter',
            field=models.IntegerField(default=0),
        ),
    ]
