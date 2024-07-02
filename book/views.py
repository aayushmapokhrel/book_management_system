from django.shortcuts import render
from book.models import Publication
# Create your views here.
def list_publication(request):
    publication = Publication.objects.filter(is_active=True)
    context = {
        "publication":publication
    }
    return render(request,'publication/index.html',context)