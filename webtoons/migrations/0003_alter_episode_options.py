# Generated by Django 3.2 on 2021-05-04 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webtoons', '0002_episode_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'ordering': ['-created_at']},
        ),
    ]
