from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='registrarse_page'),
    path('login/', views.login_view, name='iniciar_sesion_page'),
    path('logout/', views.logout_view, name='cerrar_sesion_page'),
]
