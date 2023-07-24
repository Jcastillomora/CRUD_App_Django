from django.db import models

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50, verbose_name='Nombre del Laboratorio')
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad', blank=True, null=True)
    pais = models.CharField(max_length=50, verbose_name='País', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateField(auto_now=True, verbose_name='Fecha de Modificación')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Laboratorios'
        verbose_name = 'Laboratorio'
        ordering = ['nombre']

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=50, verbose_name='Especialidad', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateField(auto_now=True, verbose_name='Fecha de Modificación')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = 'Directores Generales'
        verbose_name = 'Director General'
        ordering = ['nombre']

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = models.ForeignKey('Laboratorio', on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.CharField(max_length=4, default='2015')
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)    
    fecha_creacion = models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateField(auto_now=True, verbose_name='Fecha de Modificación')

    def __str__(self):
        return f"{self.nombre}"

    class Meta:
        verbose_name_plural = 'Productos'
        verbose_name = 'Producto'
        ordering = ['nombre']