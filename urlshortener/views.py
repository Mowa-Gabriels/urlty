from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Url
from .forms import UrlForm
from django.contrib import messages

# Create your views here.

def Index(request):
    BASE_URL = request.get_raw_uri()
    
    url = Url.objects.all()
    
    form = UrlForm()
    if request.method == 'POST':
         form = UrlForm(request.POST)
         if form.is_valid:
             print('saved!')
             form.save()
             key = form.cleaned_data.get('editable_key')
             messages.success(request, f"URL has been successfully shortened to {BASE_URL}{key}")
             return redirect('index')
         else:
             form = UrlForm

    context = {
        "BASE_URL": BASE_URL,
          
          "url" : url,
         
          "form": form,
          
        }
    return render(request, 'base.html', context)




def UrlList(request):

    url = Url.objects.all()

    context = {}

    return render(request, 'url_list.html',{"url":url})


def redirector(request, editable_key):

    instance = get_object_or_404(Url,editable_key= editable_key)
    return redirect(instance.original_url)

