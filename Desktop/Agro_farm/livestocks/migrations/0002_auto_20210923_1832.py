# Generated by Django 3.2.6 on 2021-09-23 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('livestocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.CreateModel(
            name='Livestock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livestock_name', models.CharField(max_length=200)),
                ('livestock_price', models.FloatField()),
                ('food_image', models.FileField(upload_to='static/uploads')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livestocks.category')),
            ],
        ),
    ]
