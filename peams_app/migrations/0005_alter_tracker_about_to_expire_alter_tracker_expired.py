# Generated by Django 4.2.4 on 2024-05-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peams_app', '0004_alter_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='about_to_expire',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tracker',
            name='expired',
            field=models.IntegerField(default=0),
        ),
    ]
