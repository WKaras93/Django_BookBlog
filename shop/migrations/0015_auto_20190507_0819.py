# Generated by Django 2.2.1 on 2019-05-07 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_auto_20190507_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='shop.Book'),
        ),
    ]
