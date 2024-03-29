from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_storeitems, name='store'),
    path('<int:storeitem_id>', views.storeitem_detail, name='storeitem_detail'),
    path('add/', views.add_storeitem, name='add_storeitem'),
    path('edit/<int:storeitem_id>/', views.edit_storeitem, name='edit_storeitem'),
    path('delete/<int:storeitem_id>/', views.delete_storeitem, name='delete_storeitem'),
]