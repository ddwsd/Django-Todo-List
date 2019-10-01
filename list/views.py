from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

# Create your views here.
from .forms import ListForm
from .models import List

def index(request):
    myList = List.objects.order_by('id')

    form = ListForm()

    context = { 'myList':myList, 'form':form}
    return render(request, 'index.html', context)

# @require_POST
# def addItem(request):
#     form = ListForm(request.POST)

#     if form.is_valid():
#         newList = List(listText=request.POST('text'))
#         newList.save()
    
#     return redirect('index')

def addItem(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ListForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            newList = List(listText=request.POST['text'])
            newList.save()
            # redirect to a new URL:
            return redirect('index')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ListForm()

    return render(request, 'index.html', {'form': form})

def toggleComplete(request, list_id):
    myItem = List.objects.get(pk=list_id) 
    myItem.complete = not myItem.complete
    myItem.save() 
    return redirect('index')

def deleteItem(request):
    List.objects.filter(complete__exact=True).delete()
    return redirect('index')