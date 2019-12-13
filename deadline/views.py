from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core import serializers
from django.contrib import messages
from .forms import deadlines
from .models import dl

# from reminder.forms import TodoForm
# from reminder.models import Todo
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = deadlines(request.POST)
        if form.is_valid():
            list_dl = dl()
            list_dl.nama_deadline = form.cleaned_data["daftar_deadline"]
            list_dl.save()
        return redirect('/deadline')
    else:
        form = deadlines()

        # reminder_form = TodoForm()
        # listTodo = Todo.objects.all()
        # listSize = listTodo.count()

        list_dl= dl.objects.all()
        sudah = 0
        belum = 0
        for i in list_dl:
            if(i.selesai):
                sudah += 1
            else:
                belum += 1
        context = {'form':form, 'list_dl':list_dl, 'sudah':sudah, 'belum':belum} #'rForm':reminder_form, 'listTodo':listTodo, 'listSize':listSize}
        return render(request, 'deadline/index.html', context)

def move(request, pk):
    tmp = dl.objects.get(pk=pk)
    tmp.selesai = True
    tmp.save()

    return redirect('/deadline')

def unmove(request, pk):
    tmp = dl.objects.get(pk=pk)
    tmp.selesai = False
    tmp.save()

    return redirect('/deadline')

def erase(request, pk):
    if request.method == 'POST':
        form = deadlines(request.POST)
        if form.is_valid():
            list_dl = dl()
            list_dl.nama_deadline = form.cleaned_data["daftar_deadline"]
            list_dl.save()
        return redirect('/deadline')
    else:
        dl.objects.filter(pk=pk).delete()
        form = deadlines()

        # reminder_form = TodoForm()
        # listTodo = Todo.objects.all()
        # listSize = listTodo.count()

        list_dl= dl.objects.all()
        sudah = 0
        belum = 0
        for i in list_dl:
            if(i.selesai):
                sudah += 1
            else:
                belum += 1
        context = {'form':form, 'list_dl':list_dl, 'sudah':sudah, 'belum':belum} #'rForm':reminder_form, 'listTodo':listTodo, 'listSize':listSize}
        return render(request, 'deadline/index.html', context)

def add_deadline_service(request):
    if request.method == 'POST':
        form = deadlines(request.POST)
        print(form.errors)
        print(form.is_valid())
        print(request.POST)
        if form.is_valid():
            list_dl = dl()
            list_dl.nama_deadline = form.cleaned_data["daftar_deadline"]
            list_dl.save()
            result = dl.objects.all()
            data = serializers.serialize('json', result, fields = ('nama_deadline', 'selesai'))
            return JsonResponse({'results':data})
        return JsonResponse({'message' : "error when saving the data"})

    else:
        form = deadlines()

        list_dl= dl.objects.all()
        sudah = 0
        belum = 0
        for i in list_dl:
            if(i.selesai):
                sudah += 1
            else:
                belum += 1
        context = {'form':form, 'list_dl':list_dl, 'sudah':sudah, 'belum':belum} #'rForm':reminder_form, 'listTodo':listTodo, 'listSize':listSize}
        return render(request, 'deadline/index.html', context)