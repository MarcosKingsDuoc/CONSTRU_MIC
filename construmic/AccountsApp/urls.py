from django.urls import path


from .views import (
    iniciar_sesion_page,
    registrarse_page)

# from CarritoApp.views import tienda

urlpatterns = [
    path('iniciar_sesion/', iniciar_sesion_page, name='iniciar_sesion_page'),
    path('registrarse/', registrarse_page, name='registrarse_page'),

]

