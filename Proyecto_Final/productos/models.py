from django.db import models

# Create your models here.
class Marcas(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')
    
    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre

class Tipo(models.Model):
    categoria = models.CharField(max_length=100, unique=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.categoria

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    sku = models.CharField(max_length=100, unique=True)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    modelo = models.CharField(max_length=100)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    precio = models.FloatField()
    stock = models.IntegerField()
    descuento = models.FloatField()
    novedad = models.BooleanField()    
    imagen = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    
    def __str__(self):
        return self.nombre

class Distribuidores(models.Model):
    razon_social = models.CharField(max_length=200)
    direccion = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)
    web = models.CharField(max_length=100)
    cuit=models.IntegerField(unique=True)
    descripcion = models.CharField(max_length=200, blank=True, default='')

    class Meta:
        verbose_name = 'Distribuidor'
        verbose_name_plural = 'Distribuidores'

    def __str__(self):
        return self.razon_social

class Distribuidores_Marcas(models.Model):
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    distribuidor = models.ForeignKey(Distribuidores, on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Distribuidores x marca'
        verbose_name_plural = 'Distribuidores x marcas'

    def __str__(self):
        return str(self.distribuidor)