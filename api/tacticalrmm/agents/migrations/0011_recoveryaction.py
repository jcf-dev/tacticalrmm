# Generated by Django 3.0.8 on 2020-08-09 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agents', '0010_auto_20200809_0133'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoveryAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.CharField(choices=[('salt', 'Salt'), ('mesh', 'Mesh'), ('command', 'Command')], default='mesh', max_length=50)),
                ('command', models.TextField(blank=True, null=True)),
                ('last_run', models.DateTimeField(blank=True, null=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recoveryactions', to='agents.Agent')),
            ],
        ),
    ]
