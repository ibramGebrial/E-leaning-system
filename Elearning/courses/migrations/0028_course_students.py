# Generated by Django 4.0.4 on 2022-04-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_message_recipient'),
        ('courses', '0027_remove_lesson_books_book_lessons'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='studentEnroll', to='users.profile'),
        ),
    ]
