from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home-page'),
    path('login/',views.loginPage,name='login-page'),
    path('register/',views.registerPage,name='register-page'),
    path('delete/<str:name>',views.DeleteTask,name='deleteTask-page'),
    path('logout/',views.logoutPage,name='logout-page'),
    path('update/<str:name>',views.UpdateTask,name='updateTask-page')

]
