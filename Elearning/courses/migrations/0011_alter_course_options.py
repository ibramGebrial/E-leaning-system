# Generated by Django 3.2.2 on 2022-04-19 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_course_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('created_at',)},
        ),
    ]