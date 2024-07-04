from django.shortcuts import render, redirect
from book.models import Publication, Genre
from book.forms import PublicationForm, GenreForm


# Create your views here.
def list_publication(request):
    publication = Publication.objects.filter(is_active=True)
    context = {"publication": publication}
    return render(request, "publication/index.html", context)


def create_publication(request):
    form = PublicationForm()
    if request.method == "POST":
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/book/publication/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "publication/create.html", context)


def edit_publication(request, id):
    data = Publication.objects.get(id=id)
    form = PublicationForm(instance=data)
    if request.method == "POST":
        form = PublicationForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/book/publication/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "publication/edit.html", context)


def delete_publication(request, id):
    Publication.objects.get(id=id).delete()
<<<<<<< HEAD
    return redirect('/book/publication/list')

def list_genre(request):
    genre = Genre.objects.filter(is_active=True)
    context = {'genre':genre}
    return render(request, 'genre/index.html', context)

def create_genre(request):
    form = GenreForm()
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/book/genre')
        else:
            print(form.errorrs)
        
    context = {'form':form}
    return render(request, 'genre/create.html', context)

def edit_genre(request,id):
    data = Genre.objects.get(id=id)
    form = GenreForm(instance=data)
    if request.method == 'POST':
        form = GenreForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/book/genre')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request, 'genre/edit.html', context)

def delete_genre(request,id):
    genre = Genre.objects.get(id=id).delete()
    return redirect('/book/genre')
=======
    return redirect("/book/publication/list")
>>>>>>> 9019ce4 (pr fixes)
