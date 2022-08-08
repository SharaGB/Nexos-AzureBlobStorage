import csv
import codecs
from .models import GLN_Cliente, GLN_Sucursal, Gtin_Producto, Inventario_Final
from datetime import datetime


def read_csv(file):
    # with open(file, 'r') as csvfile:
    reader = csv.reader(codecs.iterdecode(file, 'utf-8'))
    next(reader)
    for row in reader:
        date = datetime.strptime(row[0], '%m/%d/%Y')
        cliente = GLN_Cliente(nombre=row[1])
        sucursal = GLN_Sucursal(nombre_sucursal=row[2], cliente=cliente)
        producto = Gtin_Producto(
            nombre_producto=row[3], sucursal=sucursal, fecha_inventario=date.strftime('%Y-%m-%d'), precio=row[5])
        inventario = Inventario_Final(
            producto=producto, cantidad=row[4], sucursal=sucursal)
        cliente.save()
        sucursal.save()
        producto.save()
        inventario.save()
