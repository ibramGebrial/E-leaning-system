# Generated by Django 3.2.2 on 2021-11-24 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_review_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]