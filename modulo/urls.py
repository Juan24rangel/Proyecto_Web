from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='modulo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),  # Nueva ruta para el perfil
    path('videojuego/<int:videojuego_id>/', views.detalle_videojuego, name='detalle_videojuego'),
    path('favorito/agregar/<int:videojuego_id>/', views.agregar_favorito, name='agregar_favorito'),
    path('favorito/eliminar/<int:videojuego_id>/', views.eliminar_favorito, name='eliminar_favorito'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
