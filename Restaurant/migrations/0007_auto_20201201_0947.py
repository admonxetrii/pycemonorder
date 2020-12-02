# Generated by Django 3.0.4 on 2020-12-01 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0006_restologs_datentime'),
    ]

    operations = [
        migrations.CreateModel(
            name='CBMSdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cbmsusername', models.CharField(blank=True, max_length=64, null=True)),
                ('cbmspassword', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='bill',
            name='sync_ird',
        ),
        migrations.AlterField(
            model_name='billno',
            name='number',
            field=models.IntegerField(unique=True),
        ),
    ]
