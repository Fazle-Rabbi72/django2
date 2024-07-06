from django.urls import path
from .import views
urlpatterns = [
  path('add/',views.add_album,name="albumpage"),
  path('edit/<int:id>',views.edit_album, name="edit_album"),
]