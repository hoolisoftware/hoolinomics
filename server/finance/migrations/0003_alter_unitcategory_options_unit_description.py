# Generated by Django 4.1.3 on 2022-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_unitcategory_alter_currency_options_unit_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='unitcategory',
            options={'verbose_name_plural': 'unit categories'},
        ),
        migrations.AddField(
            model_name='unit',
            name='description',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]
