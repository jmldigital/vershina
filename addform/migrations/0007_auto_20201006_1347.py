# Generated by Django 3.1.1 on 2020-10-06 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addform', '0006_auto_20201006_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='customer_arrival_channel',
            field=models.CharField(blank=True, choices=[('Вебсайт', 'Вебсайт'), ('Контекстная реклама', 'Контекстная реклама'), ('Социальные сети', 'Социальные сети'), ('СМС-таргетинг', 'СМС-таргетинг'), ('Наружная реклама', 'Наружная реклама'), (' Радио', 'Радио'), ('ТВ', 'ТВ')], default='Вебсайт', max_length=50, verbose_name='Канал прихода'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_birthday',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='ДР 03/03/03'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_fb',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='в Фейсбук'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_instagram',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='в Instagram'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_odnoklassnik',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='в Однокласниках'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_smms',
            field=models.CharField(blank=True, editable=False, max_length=200, null=True, verbose_name='Социальные сети'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_tiktok',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='в Тикток'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_vkontakt',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='VK'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='customer_whatsap',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='в Вотсап'),
        ),
        migrations.AlterField(
            model_name='customers',
            name='purchase_sales',
            field=models.CharField(blank=True, max_length=10, verbose_name='Скидка в %'),
        ),
    ]
