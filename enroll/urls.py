from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.add_show,name="addshow"),
    path('staticpage/', views.static_page,name="staticpage"),
    path('delete/<int:id>/', views.delete_data,name="deletedata"),
    path('<int:id>/', views.update_data,name="updatedata"),
    path('register/', views.register_page,name="register"),
    path('login/', views.login_page,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('home/', views.dashboard,name="dashboard"),
    path('change-password/', views.change_password,name="change_password"),
    
]
