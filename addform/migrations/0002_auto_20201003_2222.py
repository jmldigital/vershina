# Generated by Django 3.1.1 on 2020-10-03 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='purchase_sales',
            field=models.CharField(blank=True, max_length=10, verbose_name='Скидка клиента в %'),
        ),
    ]
