# Generated by Django 3.2 on 2021-05-06 10:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webtoons', '0004_alter_episode_options'),
        ('interests', '0002_alter_interest_interest_webtoon_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interest',
            name='interest_webtoon_list',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='webtoons.webtoon'),
        ),
    ]