# Generated by Django 3.2.2 on 2022-04-10 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20211126_0114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('title',)},
        ),
    ]