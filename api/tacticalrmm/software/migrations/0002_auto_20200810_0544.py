# Generated by Django 3.1 on 2020-08-10 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('software', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chocosoftware',
            name='chocos',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='installedsoftware',
            name='software',
            field=models.JSONField(),
        ),
    ]
