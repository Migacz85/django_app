# Generated by Django 2.1.7 on 2019-04-11 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0009_auto_20190411_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugs',
            name='issue_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default=('Bug', 'Bug'), max_length=50),
        ),
    ]
