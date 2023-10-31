from django.shortcuts import render, HttpResponse
from . forms import AppoinmentForm
# Create your views here.

def Appoinment(request):
    if request.method == 'POST':
        form = AppoinmentForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'Message.html')
    form = AppoinmentForm()
    dict_form = {
        'form': form
    }
    return render(request, 'Form.html', dict_form)

