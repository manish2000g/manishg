# Generated by Django 3.2.6 on 2021-09-26 05:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('livestocks', '0003_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1000)])),
                ('total_price', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Delivered', 'Delivered')], max_length=200, null=True)),
                ('contact_no', models.CharField(max_length=10, null=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(10)])),
                ('contact_address', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('livestock', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='livestocks.livestock')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
