from django.urls import path

from wines import views

urlpatterns = [
    path('', views.wines_list, name='wines_list'),
    path('wine_details/<int:wine_id>/', views.wine_details, name='wine_details'),
    path('edit_wine/<int:wine_id>/', views.edit_wine, name='edit_wine'),
    path('add_grade/<int:wine_id>/', views.add_grade, name='add_grade'),
    path('add_wine/', views.add_wine, name='add_wine'),

]