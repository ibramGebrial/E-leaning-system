# Generated by Django 4.0.4 on 2022-05-05 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0039_review_title_review_user_alter_review_rate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='user',
            new_name='owner',
        ),
    ]
