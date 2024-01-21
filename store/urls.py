from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_storeitems, name='store'),
    path('<int:storeitem_id>', views.storeitem_detail, name='storeitem_detail'),
    path('add/', views.add_storeitem, name='add_storeitem'),
]