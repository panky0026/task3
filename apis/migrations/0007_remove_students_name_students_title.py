# Generated by Django 4.0.6 on 2022-09-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0006_remove_students_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='Name',
        ),
        migrations.AddField(
            model_name='students',
            name='title',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]