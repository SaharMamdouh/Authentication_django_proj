# Generated by Django 3.2.9 on 2021-11-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movie', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(to='Movie.Category'),
        ),
    ]
