# Generated by Django 2.1.7 on 2019-04-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0006_auto_20190405_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]
