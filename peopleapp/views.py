from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from peopleapp.forms import PersonForm
from .models import Person

# Create your views here.
def index_view(request):
    context={}
    context["person_list"] = Person.objects.all()
    return render(request, 'peopleapp/index_view.html', context)

def create_view(request):
    context = {}
    form = PersonForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Person Created')
            return redirect('peopleapp:people_index')       
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Person not created')

    context['form'] = form

    return render(request, 'peopleapp/create_view.html', context)

def detail_view(request, nid):
    context = {}
    # add the dictionary during initialization
    context["person"] = get_object_or_404(Person, pk=nid)
    return render(request, "peopleapp/detail_view.html", context)

def update_view(request, nid):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Person, id = nid)
    # pass the object as instance in form
    form = PersonForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'People Updated')

        return redirect('peopleapp:person_detail', nid=nid)
    # add form dictionary to context
    context["form"] = form

    return render(request, "peopleapp/update_view.html", context)

def delete_view(request, nid):
    # fetch the object related to passed id
    obj = get_object_or_404(Person, id = nid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Person Deleted')
    # after deleting redirect to index view
    return redirect('peopleapp:people_index')