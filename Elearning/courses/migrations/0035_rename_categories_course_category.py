# Generated by Django 4.0.4 on 2022-05-05 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0034_alter_category_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Categories',
            new_name='category',
        ),
    ]