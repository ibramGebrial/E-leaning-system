# Generated by Django 4.0.4 on 2022-04-25 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0019_alter_video_videolink'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='videolink',
            field=models.CharField(max_length=200),
        ),
    ]