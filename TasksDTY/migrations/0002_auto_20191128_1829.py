# Generated by Django 2.2.5 on 2019-11-28 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TasksDTY', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdty',
            name='year',
            field=models.CharField(blank=True, max_length=4),
        ),
    ]
