# Generated by Django 2.1.5 on 2019-01-19 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(choices=[('信用卡一次付清', '信用卡一次付清'), ('ATM付款', 'ATM付款'), ('退貨/退款', '退貨/退款'), ('LINE PAY', 'LINE PAY'), ('貨到付款', '貨到付款')], max_length=20, null=True)),
                ('fullName', models.CharField(max_length=128, null=True)),
                ('telephone', models.CharField(max_length=10, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('address', models.CharField(max_length=128, null=True)),
                ('pubDateTime', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'ordering': ['pubDateTime'],
            },
        ),
    ]