# Generated by Django 4.0.4 on 2022-04-29 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
        ('courses', '0029_lesson_quiz_alter_lesson_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='courses',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='quiz',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.quiz'),
        ),
    ]
