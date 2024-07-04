from django.urls import path
from book.views import (
    list_publication, 
    create_publication, 
    edit_publication,
    list_genre,
    create_genre,
    edit_genre,
    delete_genre,
)
urlpatterns = [
    path("publication",list_publication),
    path("create",create_publication),
    path("edit/<id>",edit_publication),
    path("genre",list_genre,name='list-genre'),
    path("create_genre",create_genre,name='create-genre'),
    path("edit_genre/<id>",edit_genre,name='edit-genre'),
    path("delete_genre/<id>",delete_genre,name='delete-genre'),
]