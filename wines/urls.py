from django.urls import path

from wines import views

urlpatterns = [
    path('', views.wines_list, name='wines_list'),
    path('<int:wine_id>/', views.wine_details, name='wine_details'),
]