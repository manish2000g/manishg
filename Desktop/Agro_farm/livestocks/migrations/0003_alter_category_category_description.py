# Generated by Django 3.2.6 on 2021-09-23 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livestocks', '0002_auto_20210923_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_description',
            field=models.TextField(null=True),
        ),
    ]
