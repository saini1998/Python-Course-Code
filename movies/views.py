from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # output = ' , '.join([m.title for m in movies])

    # return HttpResponse("Hello World")
    # return HttpResponse(output)
    return render(request, 'index.html', {'movies': movies})


def detail(request, movie_id):
    # try:
    # movie = Movie.objects.get(pk=movie_id)
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'detail.html', {'movie': movie})

    # except Movie.DoesNotExist:
    #     raise Http404()
