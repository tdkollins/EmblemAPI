# Generated by Django 3.0.3 on 2020-02-09 18:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fe7', '0011_auto_20200209_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='GrowthRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='growth_rates', to='fe7.Character')),
            ],
        ),
    ]
