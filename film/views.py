from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import FilmForm
from .models import Film, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


@login_required(login_url="user:login")
def dasboard(request):
    filmler = Film.objects.filter(author=request.user)
    context = {
        "filmler": filmler
    }
    return render(request, "dasboard.html", context)


@login_required(login_url="user:login")
def addfilm(request):
    form = FilmForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        film = form.save(commit=False)

        film.author = request.user
        film.save()
        messages.success(request, "Film Oluşturuldu..")
        return redirect("index")

    return render(request, "addfilm.html", {"form": form})


def detail(request, id):
    # film = Film.objects.filter(id=id).first()

    film = get_object_or_404(Film, id=id)
    comments = film.comments.all()

    return render(request, "detail.html", {"film": film, "comments": comments})


@login_required(login_url="user:login")
def updateFilm(request, id):

    film = get_object_or_404(Film, id=id)
    form = FilmForm(request.POST or None, request.FILES or None, instance=film)

    if form.is_valid():
        film = form.save(commit=False)

        film.author = request.user
        film.save()
        messages.success(request, "Film Güncellendi..")

        return redirect("index")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteFilm(request, id):

    film = get_object_or_404(Film, id=id)

    film.delete()
    messages.success(request, "Film Silindii..")

    return redirect("index")


def filmler(request):
    keyword = request.GET.get("keyword")

    if keyword:
        filmler = Film.objects.filter(title__contains=keyword)
        return render(request, "filmler.html", {"filmler": filmler})

    filmler = Film.objects.all()

    return render(request, "filmler.html", {"filmler": filmler})


def addComment(request, id):
    film = get_object_or_404(Film, id=id)

    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        if not comment_author or not comment_content:
            messages.info(request, "Lütfen tüm alanları doldurun.")
        else:
            newComment = Comment(comment_author=comment_author,
                                 comment_content=comment_content)
            newComment.film = film
            newComment.save()

    return redirect("/filmler/film/"+str(id))
