# Generated by Django 3.2 on 2021-05-04 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("webtoons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="episode",
            name="title",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
