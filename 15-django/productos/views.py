from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto


# def index(request):
# Retorna todos los elementos
# productos = Producto.objects.all()
# productos = Producto.objects.all().values()

# Filtra por puntaje igual a 3
# productos = Producto.objects.filter(puntaje=3)

# Filtra por puntaje mayor o igual a 3
# productos = Producto.objects.filter(puntaje__gte=3)

# Filtra por id igual a 1
# productos = Producto.objects.get(id=1)
# print(productos)
# return JsonResponse(list(productos), safe=False)

def index(request):
    productos = Producto.objects.all()

    return render(
        request,
        'productos.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    
    return render(
        request,
        'detalle.html',
        context={'producto': producto}
    )
