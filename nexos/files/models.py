from django.db import models
from django.core.validators import FileExtensionValidator


class Files(models.Model):
    file = models.FileField(
        upload_to='files/', validators=[FileExtensionValidator(allowed_extensions=['csv'])])


class GLN_Cliente(models.Model):
    """ Código que identifica el Cliente"""
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)


class GLN_Sucursal(models.Model):
    """ Código que identifica la Sucursal """
    nombre_sucursal = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    cliente = models.ForeignKey(GLN_Cliente, on_delete=models.CASCADE)


class Gtin_Producto(models.Model):
    """ Código que identifica el producto inventariado """
    nombre_producto = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=150)
    precio = models.DecimalField(
        "Es el precio base de la Unidad inventariada",
        max_digits=10,
        decimal_places=2
    )
    sucursal = models.ForeignKey(GLN_Sucursal, on_delete=models.CASCADE)
    fecha_inventario = models.DateField(
        "Fecha en la cual se toma el inventario del producto",
        # auto_now_add=True
    )


class Inventario_Final(models.Model):
    """ Cantidad inventariada """
    producto = models.ForeignKey(Gtin_Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    sucursal = models.ForeignKey(GLN_Sucursal, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=150)
