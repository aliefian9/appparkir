# Generated by Django 3.1.7 on 2021-04-04 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkir', '0003_auto_20210403_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jumlah',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('Tersedia', models.IntegerField()),
            ],
        ),
    ]
