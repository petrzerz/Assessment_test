# Generated by Django 3.0.8 on 2020-07-23 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstoreapi', '0003_author_billing_book_cashier_category_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField()),
                ('bookName', models.CharField(max_length=100)),
                ('categoryID', models.CharField(max_length=100)),
            ],
        ),
    ]
