from django.urls import path
from . import views

app_name = 'tickets'

urlpatterns = [
    # Tickets
    path('', views.TicketListView.as_view(), name='ticket_list'),
    path('ticket/<int:pk>/', views.TicketDetailView.as_view(), name='ticket_detail'),
    path('ticket/crear/', views.TicketCreateView.as_view(), name='ticket_create'),
    path('ticket/<int:pk>/editar/', views.TicketUpdateView.as_view(), name='ticket_update'),
    path('ticket/<int:pk>/eliminar/', views.TicketDeleteView.as_view(), name='ticket_delete'),

    # Usuarios
    path('usuarios/', views.UsuarioListView.as_view(), name='usuario_list'),
    path('usuario/crear/', views.UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuario/<int:pk>/editar/', views.UsuarioUpdateView.as_view(), name='usuario_update'),
    path('usuario/<int:pk>/eliminar/', views.UsuarioDeleteView.as_view(), name='usuario_delete'),
]
