from django.shortcuts import render, redirect, HttpResponse 
from .forms import LaboratorioForm
from .models import Laboratorio, DirectorGeneral, Producto

# Create your views here.
def insertar_lab_view(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/mostrar/')
    form = LaboratorioForm()
    context = {'form':form}
    return render(request, 'insertar.html', context)


def mostrar_lab_view(request):
    laboratorios = Laboratorio.objects.all()
    num_visitas =request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visitas+1
    context = {
        'laboratorios': laboratorios,
        'num_visitas':num_visitas,
    }
    return render(request, 'mostrar.html', context)

def editar_lab_view(request, pk):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        print(request.POST)
        if form.is_valid():
            laboratorio = Laboratorio.objects.get(id=pk)
            laboratorio.nombre = request.POST['nombre']
            laboratorio.ciudad = request.POST['ciudad']
            laboratorio.pais = request.POST['pais']
            laboratorio.save()
            return redirect('/mostrar/')
    laboratorio = Laboratorio.objects.get(id=pk)
    form = LaboratorioForm(instance=laboratorio)
    context = {'form':form, 'laboratorio':laboratorio} 
    return render(request, 'editar.html',context)


def eliminar_lab_view(request,pk):
    laboratorio = Laboratorio.objects.get(id=pk)
    if request.method == "POST":
        laboratorio.delete()

        return redirect('/mostrar/')
    context={'laboratorio':laboratorio}
    return render(request, 'eliminar.html', context)

# def empleado_detalle_view(request, pk):
#     empleado = Empleado.objects.get(id=pk)
#     context = {'empleado':empleado}
#     return render(request, 'crudapp/detalle.html',context=context)