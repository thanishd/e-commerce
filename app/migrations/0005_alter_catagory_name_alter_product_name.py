# Generated by Django 4.2.5 on 2023-10-03 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='name',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=300),
        ),
    ]
