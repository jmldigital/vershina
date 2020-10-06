from django.shortcuts import render
from addform.models import *

def customers_table(request):

    customers_numb = Customers.objects.all()
    customers_social = customers_numb.values('customer_vkontakt', 'customer_odnoklassnik','customer_tiktok','customer_fb','customer_whatsap','customer_instagram')


    socials = []
    ii = 0
    dd = 0

    for ite in customers_social:
        d2 = customers_social[ii]
        d = {k: v for k, v in d2.items() if v != None}
        # d = str(d)
        socials.append(d)
        customer_smms = ite
        ii = ii + 1


    ss = customers_numb.count






    # soxx = customers_social[0].value('customer_vkontakt')

    # socials = [x for x in socials if x]
    # result = '; '.join([f'{key.capitalize()}: {value}' for key, value in socials[0].items()])
    lent = len(socials)
    # customer_social = customers_numb.exclude(customer_odnoklassnik=None)
    # result = str(test1)
    # customer_social = customers_numb.exclude(customer_tiktok=None)


    return render(request,'customers/customers.html',locals())