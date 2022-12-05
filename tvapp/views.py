from django.shortcuts import (render, redirect, get_object_or_404)
from django.contrib import messages
from tvapp.forms import SeriesForm, SeasonForm, EpisodeForm
from .models import Series, Season, Episode

# Create your views here.
def index_view(request):
    context={}
    context["series_list"] = Series.objects.all()
    return render(request, 'tvapp/index_view.html', context)

def create_series_view(request):
    context = {}
    form = SeriesForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Series Created')
            return redirect('tvapp:tv_library')       
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Series not created')

    context['form'] = form

    return render(request, 'tvapp/create_view.html', context)

def create_season_view(request, nid):
    context = {}
    form = SeasonForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.series = Series.objects.get(pk=nid)
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Season Created')
            return redirect('tvapp:detailed_series_view', nid)       
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Season not created')

    context['form'] = form

    return render(request, 'tvapp/create_view.html', context)

def create_episode_view(request, nid, seid):
    context = {}
    form = EpisodeForm(request.POST or None)
    if (request.method == 'POST'):
        if form.is_valid():
            obj = form.save(commit=False)
            obj.season = Season.objects.get(pk=seid)
            obj.save()
            messages.add_message(request, messages.SUCCESS, 'Episode Created')
            return redirect('tvapp:detailed_season_view', nid, seid)       
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Form Data; Episode not created')

    context['form'] = form

    return render(request, 'tvapp/create_view.html', context)

def detailed_series_view(request, nid):
    context ={}
    # add the dictionary during initialization
    series = get_object_or_404(Series, pk=nid)
    context["series"] = series
    context["seasons"] = Season.objects.filter(series__pk=nid)
    return render(request, "tvapp/detailed_series_view.html", context)

def detailed_season_view(request, nid, seid):
    context ={}
    # add the dictionary during initialization
    context["series"] = get_object_or_404(Series, pk=nid)
    season = get_object_or_404(Season, pk=seid)
    context["season"] = season
    context["episodes"] = season.episodes.all()
    return render(request, "tvapp/detailed_season_view.html", context)

def detailed_episode_view(request, nid, seid, eid):
    context ={}
    # add the dictionary during initialization
    context["series"] = get_object_or_404(Series, pk=nid)
    season = get_object_or_404(Season, pk=seid)
    episode = get_object_or_404(Episode, pk = eid)
    context["season"] = season
    context["episode"] = episode
    return render(request, "tvapp/detailed_episode_view.html", context)

def update_series_view(request, nid):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Series, id = nid)
    # pass the object as instance in form
    form = SeriesForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Series Updated')

        return redirect('tvapp:detailed_series_view', nid=nid)
    # add form dictionary to context
    context["form"] = form

    return render(request, "tvapp/update_view.html", context)

def update_season_view(request, nid, seid):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Season, id = seid)
    # pass the object as instance in form
    form = SeasonForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Season Updated')

        return redirect('tvapp:detailed_season_view', nid=nid, seid=seid)
    # add form dictionary to context
    context["form"] = form

    return render(request, "tvapp/update_view.html", context)

def update_episode_view(request, nid, seid, eid):
    context ={}

    # fetch the object related to passed id
    obj = get_object_or_404(Episode, id = eid)
    # pass the object as instance in form
    form = EpisodeForm(request.POST or None, instance = obj)
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 'Episode Updated')

        return redirect('tvapp:detailed_episode_view', nid=nid, seid=seid, eid=eid)
    # add form dictionary to context
    context["form"] = form

    return render(request, "tvapp/update_view.html", context)


def delete_series_view(request, nid):
    # fetch the object related to passed id
    obj = get_object_or_404(Series, id = nid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Series Deleted')
    # after deleting redirect to index view
    return redirect('tvapp:tv_library')

def delete_season_view(request, nid, seid):
    # fetch the object related to passed id
    obj = get_object_or_404(Season, id = seid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Season Deleted')
    # after deleting redirect to index view
    return redirect('tvapp:detailed_series_view', nid = nid)

def delete_episode_view(request, nid, seid, eid):
    # fetch the object related to passed id
    obj = get_object_or_404(Episode, id = eid)
    # delete object
    obj.delete()
    messages.add_message(request, messages.SUCCESS, 'Episode Deleted')
    # after deleting redirect to index view
    return redirect('tvapp:detailed_season_view', nid = nid, seid = seid)