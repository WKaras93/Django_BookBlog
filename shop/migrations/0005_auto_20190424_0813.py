# Generated by Django 2.2 on 2019-04-24 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20190424_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publishing_year',
            new_name='publication_date',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publishing_house',
            new_name='publisher',
        ),
    ]
