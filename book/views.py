from django.shortcuts import render, redirect
from book.models import Publication
from book.forms import PublicationForm

# Create your views here.
def list_publication(request):
    publication = Publication.objects.filter(is_active=True)
    context = {
        "publication":publication
    }
    return render(request,'publication/index.html',context)


def create_publication(request):
    form = PublicationForm()
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book/publication')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request,'publication/create.html',context)

def edit_publication(request,id):
    data = Publication.objects.get(id=id)
    form = PublicationForm(instance=data)
    if request.method == 'POST':
        form = PublicationForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/book/publication')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request,'publication/edit.html',context)

def delete_publication(request,id):
    publication = Publication.objects.get(id=id).delete()
    return redirect('')