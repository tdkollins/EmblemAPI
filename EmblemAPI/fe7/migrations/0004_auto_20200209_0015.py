# Generated by Django 3.0.3 on 2020-02-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fe7', '0003_auto_20200208_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestats',
            name='constitution',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='defence',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='luck',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='magic',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='move',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='resistance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='skill',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='basestats',
            name='strength',
            field=models.IntegerField(default=0),
        ),
    ]
