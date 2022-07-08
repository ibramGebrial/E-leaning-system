# Generated by Django 4.0.4 on 2022-04-29 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_remove_lesson_quiz'),
        ('quiz', '0005_alter_quiz_lesson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.lesson'),
        ),
    ]
