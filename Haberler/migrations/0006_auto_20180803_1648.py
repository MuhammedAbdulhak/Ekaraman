# Generated by Django 2.0 on 2018-08-03 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haberler', '0005_auto_20180803_1501'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterField(
            model_name='article',
            name='published_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(on_delete=None, to='Haberler.Category', verbose_name='Ebeveyn kategori'),
        ),
    ]
