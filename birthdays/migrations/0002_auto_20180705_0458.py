# Generated by Django 2.0 on 2018-07-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthdays', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='bday_date',
            field=models.CharField(max_length=6),
        ),
    ]
