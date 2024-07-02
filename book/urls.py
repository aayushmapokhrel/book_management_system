from django.urls import path
from book.views import list_publication
urlpatterns = [
    path("publication",list_publication)
]