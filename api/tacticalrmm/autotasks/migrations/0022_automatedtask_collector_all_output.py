# Generated by Django 3.2.1 on 2021-05-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotasks', '0021_alter_automatedtask_custom_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='automatedtask',
            name='collector_all_output',
            field=models.BooleanField(default=False),
        ),
    ]
