# Generated by Django 4.2.8 on 2024-02-27 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0010_workoutlog_r1_workoutlog_r2_workoutlog_r3_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutlog',
            name='mail',
            field=models.EmailField(default='kumudal19@gmail.com', max_length=254),
        ),
    ]
