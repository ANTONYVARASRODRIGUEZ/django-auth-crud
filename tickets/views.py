from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ticket, Usuario
from .forms import TicketForm, UsuarioForm


# ======================
# CRUD DE USUARIOS
# ======================
class UsuarioListView(ListView):
    model = Usuario
    template_name = 'tickets/usuario_list.html'
    context_object_name = 'usuarios'


class UsuarioCreateView(CreateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'tickets/usuario_form.html'
    success_url = reverse_lazy('tickets:usuario_list')


class UsuarioUpdateView(UpdateView):
    model = Usuario
    form_class = UsuarioForm
    template_name = 'tickets/usuario_form.html'
    success_url = reverse_lazy('tickets:usuario_list')


class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'tickets/usuario_confirm_delete.html'
    success_url = reverse_lazy('tickets:usuario_list')


# ======================
# CRUD DE TICKETS
# ======================
class TicketListView(ListView):
    model = Ticket
    template_name = 'tickets/ticket_list.html'
    context_object_name = 'tickets'


class TicketDetailView(DetailView):
    model = Ticket
    template_name = 'tickets/ticket_detail.html'


class TicketCreateView(CreateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('tickets:ticket_list')


class TicketUpdateView(UpdateView):
    model = Ticket
    form_class = TicketForm
    template_name = 'tickets/ticket_form.html'
    success_url = reverse_lazy('tickets:ticket_list')


class TicketDeleteView(DeleteView):
    model = Ticket
    template_name = 'tickets/ticket_confirm_delete.html'
    success_url = reverse_lazy('tickets:ticket_list')
