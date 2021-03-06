# Generated by Django 2.2 on 2019-04-26 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0009_auto_20190426_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='create',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='book',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='shop.Book'),
            preserve_default=False,
        ),
    ]
