# Generated by Django 3.1.7 on 2021-04-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkir', '0004_jumlah'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jumlah',
            name='Tersedia',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='parkir',
            name='Status',
            field=models.IntegerField(default=0),
        ),
    ]
