# Generated by Django 4.0.6 on 2022-09-20 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0019_rename_student_studentrecode'),
    ]

    operations = [
        migrations.DeleteModel(
            name='studentrecode',
        ),
    ]
