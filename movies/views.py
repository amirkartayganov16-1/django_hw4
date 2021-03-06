from django.shortcuts import render, Http404,HttpResponse
from .models import Director, Movie, Review


# def test1(request):
#     dict_ = {
#         'title': 'Blog APPLICATION',
#         'text': 'HELLO WORLD!',
#         'date': ''
#     }
#     return render(request, 'movie.html', context=dict_)

def movie_list_view(request):
    movie_list = Movie.objects.all()
    context = {
        'movie': movie_list
    }
    return render(request, 'movie.html', context=context)

def movie_detail_view(request, id):
    try:
        movie_detail = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        raise Http404('Critical error! Id must start with 2!')
    review = Review.objects.filter(movie_id=id)
    return render(request, 'movie_detail_view.html', context={
        'detail': movie_detail,
        'review': review
    })