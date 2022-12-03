from django.shortcuts import render

# Create your views here.
def index_view(request):
    context={}
    context["movie_list"] = Movie.objects.all()
    return render(request, 'movieapp/index_view.html', context)

def create_view(request):
    context = {}
    