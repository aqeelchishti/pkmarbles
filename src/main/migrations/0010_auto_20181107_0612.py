# Generated by Django 2.0 on 2018-11-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20181107_0609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.IntegerField(choices=[(0, 'All Categories'), (1, 'Granite'), (2, 'Marble'), (3, 'Onyx'), (4, 'Handicraft')], default=0),
        ),
    ]
