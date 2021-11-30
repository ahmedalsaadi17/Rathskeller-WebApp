# Generated by Django 3.2.9 on 2021-11-30 11:11

from django.db import migrations, models
import django.db.models.deletion
import order.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rath', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default=order.models.order_id_generator, max_length=11, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('items', models.ManyToManyField(to='rath.Item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='order.order')),
            ],
        ),
    ]