# Generated by Django 4.0.6 on 2022-09-20 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0010_delete_studentmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]