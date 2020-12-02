# Generated by Django 3.0.4 on 2020-12-02 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0008_auto_20201201_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cbmsdata',
            name='cbmsusername',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.CreateModel(
            name='BillSync',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sync_ird', models.BooleanField(blank=True, null=True)),
                ('bill', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Restaurant.Bill')),
            ],
        ),
    ]
