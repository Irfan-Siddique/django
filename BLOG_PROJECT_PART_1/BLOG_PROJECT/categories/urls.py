from django.urls import path
from . import views
urlpatterns = [
    path('add/',views.addCategoryForm, name='add_category')
]
