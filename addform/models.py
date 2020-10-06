from django.db import models

class Customers(models.Model):

    WEBSITE = 'Вебсайт'
    CONTEXT = 'Контекстная реклама'
    SOCIALNET = 'Социальные сети'
    SMSTAG = 'СМС-таргетинг'
    MEDIABORD = 'Наружная реклама'
    RADIO = ' Радио'
    TV = 'ТВ'

    CASHH = 'Наличные'
    NONCASH = 'Безналичный'
    WEBSITEPAY = 'Через сайт'
    CREDITT = 'Кредит'
    SUBSCR = 'Рассрочка'
    OTHERS = 'Другой способ'

    PAYPAL = 'Пайпал'
    YKASSA = 'Яндекс касса'
    SOCIALNETPAY = 'Социальные сети'

    SELPHONE = 'Телефон'
    SELFPOST = 'Почта'
    INSTA = 'Инстаграм'
    VK = 'Вконтакте'
    ODNOKL = 'Одноклассники'
    TIKTOK = 'Тикток'
    WHATSAP = 'Вотсап'
    FB = 'Фейсбук'


    CUSTOMER_ARRIVAL_CHANNEL = [
        (WEBSITE, 'Вебсайт'),
        (CONTEXT, 'Контекстная реклама'),
        (SOCIALNET, 'Социальные сети'),
        (SMSTAG, 'СМС-таргетинг'),
        (MEDIABORD, 'Наружная реклама'),
        (RADIO, 'Радио'),
        (TV, 'ТВ'),
    ]

    CUSTOMER_PURCHASE_TYPE = [
        (CASHH, 'Наличные'),
        (NONCASH, 'Безналичный'),
        (WEBSITEPAY, 'Через сайт'),
        (CREDITT, 'Кредит'),
        (SUBSCR, 'Рассрочка'),
        ('Другой способ',(
            ( PAYPAL, 'Пайпал'),(YKASSA, 'Яндекс касса'),( SOCIALNETPAY, 'Социальные сети')
        ))
    ]

    CUSTOMER_CONTACTS = [
        (SELPHONE, 'Телефон'),
        (SELFPOST, 'Почта'),
        ('Соцсети',(
            ( INSTA,'Инстаграм'),(VK,'Вконтакте'),( ODNOKL,'Одноклассники'),( TIKTOK,'Тикток'),( WHATSAP,'Вотсап'),( FB,'Фейсбук')
        ))
    ]

    customer_arrival_channel = models.CharField(
        max_length=50,
        choices=CUSTOMER_ARRIVAL_CHANNEL,
        default=WEBSITE,
        blank=True,
        verbose_name = 'Канал прихода'
    )

    purchase_sales = models.CharField(
        max_length=10,
        blank=True,
        verbose_name='Скидка в %'
    )

    purchase_detail = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Сумма/кол-во'
    )

    purchase_detail_type = models.CharField(
        max_length=50,
        choices=CUSTOMER_PURCHASE_TYPE,
        default=CASHH,
        blank=True,
        verbose_name='Как платит'
    )

    customer_phone = models.CharField(
        null=True,
        max_length=15,
        blank=True,
        verbose_name='Телефон клиента'
    )

    customer_post = models.EmailField(
        null=True,
        blank=True,
        verbose_name='Почта клиента'
    )

    customer_vkontakt = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='VK'
    )

    customer_odnoklassnik = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='в Однокласниках'
    )

    customer_instagram = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='в Instagram'
    )

    customer_tiktok = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='в Тикток'
    )

    customer_fb = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='в Фейсбук'
    )

    customer_whatsap = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='в Вотсап'
    )

    customer_fio = models.CharField(
        null=True,
        max_length=20,
        blank=True,
        verbose_name='ФИО'
    )

    customer_address = models.CharField(
        null=True,
        max_length=80,
        blank=True,
        verbose_name='Адрес'
    )

    customer_birthday = models.CharField (
        max_length=20,
        null=True,
        blank=True,
        verbose_name='ДР 03/03/03'
    )

    customer_smms = models.CharField (
        max_length=200,
        editable=False,
        null=True,
        blank=True,
        verbose_name='Социальные сети'
    )

    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.customer_fio

    def smm(self):
        return '%s %s %s %s %s %s' % (self.customer_vkontakt, self.customer_fb, self.customer_instagram, self.customer_tiktok,  self.customer_odnoklassnik, self.customer_whatsap,)

    smm_list = property(smm)


    def save(self, *args, **kwargs):

        smm_list = Customers.smm(self).split()

        dd = [x for x in smm_list if x != "None"]
        ss = "<br>".join(dd)

        self.customer_smms = ss
        super(Customers, self).save(*args, **kwargs)


    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"