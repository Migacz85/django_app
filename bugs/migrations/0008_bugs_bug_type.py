# Generated by Django 2.1.7 on 2019-04-11 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0007_auto_20190408_1130'),
    ]

    operations = [
        migrations.AddField(
            model_name='bugs',
            name='bug_type',
            field=models.CharField(choices=[('Bug', 'Bug'), ('Issue', 'Issue')], default=('Bug', 'Bug'), max_length=50),
        ),
    ]
