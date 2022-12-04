from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from movieapp.forms import MovieForm
from .models import Movie

# Create your views here.
def index_view(request):
    context={}
    context["movie_list"] = Movie.objects.all()
    return render(request, 'movieapp/index_view.html', context)

def create_view(request):
    context = {}
    form = MovieForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Movie Created')
            return redirect('movie_library')       
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Movie not created')

    context['form'] = form

    return render(request, 'movieapp/create_view.html', context)
    
def detail_view(request, nid):
    context ={}
    # add the dictionary during initialization
    context["movie"] = get_object_or_404(Movie, pk=nid)
    return render(request, "movieapp/detail_view.html", context)

def update_view(request, nid):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Movie, id = nid)
    # pass the object as instance in form
    form = MovieForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Movie Updated')

        return redirect('movieapp:movie_detail', nid=nid)
    # add form dictionary to context
    context["form"] = form

    return render(request, "movieapp/update_view.html", context)

def delete_view(request, nid):
    # fetch the object related to passed id
    obj = get_object_or_404(Movie, id = nid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Movie Deleted')
    # after deleting redirect to index view
    return redirect('movieapp:movie_library')