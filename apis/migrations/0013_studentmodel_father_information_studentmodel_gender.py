# Generated by Django 4.0.6 on 2022-09-20 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0012_rename_title_studentmodel_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmodel',
            name='father_information',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='studentmodel',
            name='gender',
            field=models.CharField(max_length=20, null=True),
        ),
    ]