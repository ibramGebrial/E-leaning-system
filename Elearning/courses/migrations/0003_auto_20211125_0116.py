# Generated by Django 3.2.2 on 2021-11-24 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211125_0114'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Ibram',
        ),
        migrations.RemoveField(
            model_name='review',
            name='course',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
