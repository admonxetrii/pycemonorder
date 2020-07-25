# Generated by Django 3.0.4 on 2020-05-07 13:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0002_auto_20200402_1844'),
    ]

    operations = [
        migrations.CreateModel(
            name='TableDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disval', models.FloatField(blank=True, null=True)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Table')),
            ],
        ),
    ]