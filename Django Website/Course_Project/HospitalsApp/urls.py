# import path function from django.urls
from django.urls import path

# import views.py from the current folder
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('add/', views.add_new_hospital, name='add_new_student'),
    path('list/', views.list_hospitals, name='list_hospitals'),
    path('list/<str:pk>', views.list_hospitals, name='list_hospitals'),
    path('search/', views.search_hospital, name='search_hospital'),
    path('update/', views.update_hospital, name='update_hospital'),
    path('update/<str:pk>', views.update_hospital, name='update_hospital'),
    path('delete/', views.delete_hospital, name='delete_hospital'),
    path('delete/<str:pk>', views.delete_hospital, name='delete_hospital'),
    path('registration/', views.registration_page, name='registration'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('email/', views.email, name='email'),
]