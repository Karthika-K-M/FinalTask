from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movies, Review
from .forms import MoviesForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def demo(request):
    category = request.GET.get('category')

    if category:
        # Filter movies based on the selected category
        obj = Movies.objects.filter(category=category)
    else:
        # If no category is selected, retrieve all movies
        obj = Movies.objects.all()
    context = {
        'movie_list': obj
    }
    return render(request, 'index.html', context)
# Create your views here.
@login_required
def add_movies(request):
    if request.method == "POST":
        title = request.POST.get('title', )
        img = request.FILES['img']
        desc = request.POST.get('desc', )
        releasedate = request.POST.get('releasedate', )
        actors = request.POST.get('actors', )
        category = request.POST.get('category', )
        trailer = request.POST.get('trailer', )
        user = request.user
        movie = Movies(title=title, desc=desc, releasedate=releasedate, img=img, actors=actors,category=category,trailer=trailer,user=user)
        movie.save()
    return render(request, 'add.html')
@login_required
def details(request, movie_id):
    movie = Movies.objects.get(id=movie_id)
    return render(request, "detail.html", {'movie': movie})
@login_required
def edit_movie(request, id):
    movie = Movies.objects.get(id=id)
    if request.method == 'POST' :
        form = MoviesForm(request.POST or None, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = MoviesForm(instance=movie)
    return render(request, 'editform.html', {'form': form, 'movie': movie})
@login_required
def delete(request, id):
    if request.method == "POST":
        movie = Movies.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')

@login_required
def add_review(request):
    if request.method == 'POST':
        movie_id = request.POST['movie_id']
        content = request.POST['review_content']
        movie = Movies.objects.get(pk=movie_id)
        # Create a new review associated with the movie and current user
        review = Review.objects.create(movie=movie, user=request.user, content=content)
        messages.success(request, 'Your review has been added successfully.')
    return redirect('/')  # Redirect to the same page after adding review


def search_results(request):
    query = request.GET.get('q')
    if query:
        # Perform search based on the query
        results = Movies.objects.filter(title__icontains=query)
    else:
        results = None

    return render(request, 'search_results.html', {'results': results, 'query': query})