# Generated by Django 2.0 on 2018-08-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haberler', '0007_auto_20180803_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hash_tags',
            field=models.ManyToManyField(blank=True, default=None, to='Haberler.HashTag'),
        ),
    ]
