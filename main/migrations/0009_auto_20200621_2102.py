# Generated by Django 3.0.2 on 2020-06-21 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200621_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtweet',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
    ]
