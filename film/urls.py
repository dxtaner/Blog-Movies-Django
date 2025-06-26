from django.contrib import admin
from django.urls import path
from .import views

app_name = "filmapp"


urlpatterns = [
    path('dasboard/', views.dasboard, name="dasboard"),
    path('addfilm/', views.addfilm, name="addfilm"),
    path('film/<int:id>', views.detail, name="detail"),
    path('update/<int:id>', views.updateFilm, name="update"),
    path('delete/<int:id>', views.deleteFilm, name="delete"),
    path('', views.filmler, name="filmler"),
    path('comment/<int:id>', views.addComment, name="comment"),
]
