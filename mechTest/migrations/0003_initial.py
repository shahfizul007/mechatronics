# Generated by Django 5.1.1 on 2024-09-26 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mechTest', '0002_delete_owner_delete_product_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.TextField()),
                ('order_id', models.IntegerField()),
                ('food_order', models.TextField()),
            ],
        ),
    ]
