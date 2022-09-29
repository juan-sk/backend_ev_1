

from django.http import HttpResponse
from django.shortcuts import render

from backend_ev_1.dominio.clases.Reserva import Reserva


def inicio(request):
    return render(request,"inicio.html")

def ingresoReserva(request):
    return render( request,"ingreso_reserva.html")
def paginaMostrarDatos(request):
    
    nombre= request.POST["txtnombre"]
    rut= request.POST["txtrut"]
    sexo= request.POST["txtSexo"]
    nacimiento= request.POST["txtfechanacimiento"]
    reserva= request.POST["txtfechareserva"]
    telefono_contacto= request.POST["txttelefonocontacto"]
    nro_habitacion= request.POST["txthabitacoin"]
    r = Reserva(
        nombre,
        rut,
        sexo,
        nacimiento,
        reserva,
        telefono_contacto,
        nro_habitacion
    )
    return render(request,'datos_reserva.html',{'r':r})
def paginaMostrarDatos2(request):

    nombre= request.GET["txtnombre"]
    rut= request.GET["txtrut"]
    sexo= request.GET["txtSexo"]
    nacimiento= request.GET["txtfechanacimiento"]
    reserva= request.GET["txtfechareserva"]
    telefono_contacto= request.GET["txttelefonocontacto"]
    nro_habitacion= request.GET["txthabitacoin"]
    r = Reserva(
        nombre,
        rut,
        sexo,
        nacimiento,
        reserva,
        telefono_contacto,
        nro_habitacion
    )
    return render(request,'datos_reserva.html',{'r':r})

def buscarActualizarReserva(request):
    return render( request,"buscar_actualizar.html")
def actualizarReserva(request):
    id = request.GET["txtid"]
    return render( request,"actualizar_reserva.html",{"id":id})


def buscarEliminarReserva(request):
 
    
    return render(request, "buscar_eliminar.html")

def eliminarReserva(request):
    id = request.POST["txtid"]
    
    return render(request, "eliminar.html",{"id":id})


def listarregistros(request):
       return render(request, "listar.html")

def buscarReserva(request):
       return render(request, "busqueda_reserva.html")

def reservaPorDefecto(request):
    id = request.GET["txtid"]
    return render(request, "reservaPorDefecto.html",{"id":id})
