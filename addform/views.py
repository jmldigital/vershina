from django.shortcuts import render
from .forms import AddCustomerForm
from .models import *

def addform(request):

    form = AddCustomerForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        new_form = form.save()


    return render(request, 'addform/addform.html', locals())