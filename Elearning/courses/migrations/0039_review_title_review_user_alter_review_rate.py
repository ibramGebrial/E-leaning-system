# Generated by Django 4.0.4 on 2022-05-05 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_message_recipient'),
        ('courses', '0038_alter_category_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.FloatField(default=0),
        ),
    ]
