# Generated by Django 2.0 on 2018-07-05 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Birthday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bday_name', models.CharField(max_length=300)),
                ('bday_date', models.IntegerField()),
            ],
        ),
    ]
