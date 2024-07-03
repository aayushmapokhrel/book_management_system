from django.urls import path
from book.views import list_publication, create_publication, edit_publication
urlpatterns = [
    path("publication",list_publication),
    path("create",create_publication),
    path("edit/<id>",edit_publication),
]