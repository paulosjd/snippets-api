# Generated by Django 2.1.7 on 2019-04-05 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_auto_20190405_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='markdownsegment',
            name='order',
            field=models.IntegerField(db_index=True, help_text='Int asc. order'),
        ),
        migrations.AlterUniqueTogether(
            name='markdownsegment',
            unique_together={('order', 'topic')},
        ),
    ]