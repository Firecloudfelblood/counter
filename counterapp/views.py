from django.shortcuts import render, redirect
from .models import CounterModel

# Create your views here.

def helloworld(request):
    name = "MaGyo"
    obj = CounterModel.objects.filter(id=1)[0]
    number = obj.number
    context = {'name': name, 'number': number}
    return render(request, "helloworld/helloworld.html", context)

def increment(request):
    #here will increment
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number )+ 1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    #here will decrement
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = int(obj.number) -1
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    #here will reset
    obj = CounterModel.objects.filter(id=1)[0]
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

