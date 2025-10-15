from django.db import models

# Modelo Usuario (tabla relacionada)
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    rol = models.CharField(max_length=50, default='cliente')

    def __str__(self):
        return self.nombre


# Modelo Ticket (tabla principal)
class Ticket(models.Model):
    ESTADOS = [
        ('nuevo', 'Nuevo'),
        ('en_progreso', 'En progreso'),
        ('resuelto', 'Resuelto'),
        ('cerrado', 'Cerrado'),
    ]

    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='tickets_imagenes/', blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='nuevo')
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='tickets')
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.asunto} - {self.get_estado_display()}"
