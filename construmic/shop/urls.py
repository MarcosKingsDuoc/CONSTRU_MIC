from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/', views.ver_carrito, name='carrito'),
    path('comprar/', views.comprar, name='comprar'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('cambiar_cantidad/<int:producto_id>/<str:operacion>/', views.cambiar_cantidad_producto, name='cambiar_cantidad_producto'),
    path('admin/historial/', views.admin_historial_compras, name='admin_historial_compras'),
    path('admin/agregar_producto/', views.admin_agregar_producto, name='admin_agregar_producto'),
]

handler403 = 'shop.views.error_403'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
