from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import DescripcionMensaje 
from .forms import MensajesForm
from django.contrib.auth import login
from .forms import RegistroForm
from django.db.models import Q#importar para hacer consultas complejas

# Create your views here.

#CREAR MENSAJES
#FBV
@login_required #solo para los usuarios autenticados
def crear_mensaje(request):
    if request.method=='POST':
        form=MensajesForm(request.POST)
        if form.is_valid():
            mensaje= form.save(commit=False)
            mensaje.remitente= request.user #asigna el remitente como el usuario autenticado
            mensaje.save()
            return redirect("mensajes_enviados")
    else:
        form=MensajesForm()#si no es post muestra el formulario vacio
    return render(request, "mensajes/crear_mensaje.html", {"form":form})
#CBV
class crearMensajeView(CreateView):
    model=DescripcionMensaje
    form_class=MensajesForm
    template_name="mensajes/crear_mensaje.html"
    success_url=reverse_lazy("mensajes_enviados")

    def form_valid(self, form):
        form.instance.remitente=self.request.user#asigna el remitente
        return super().form_valid(form)
#VER MENSAJES 
#mensajes recibidos
@login_required
def mensajes_recibidos(request):
    mensajes=DescripcionMensaje.objects.filter(destinatario=request.user)
    return render(request,"mensajes/mensajes_recibidos.html", {"mensajes": mensajes})
#mensajes enviados
@login_required
def mensajes_enviados(request):
    mensajes=DescripcionMensaje.objects.filter(remitente=request.user)
    return render(request,"mensajes/mensajes_enviados.html", {"mensajes": mensajes})

#ELIMINAR MENSAJES
@login_required
def eliminar_mensaje(request, mensaje_id):
    mensaje = get_object_or_404(DescripcionMensaje, Q(remitente=request.user)| Q(destinatario=request.user), id=mensaje_id)
    if request.method =="POST":
        mensaje.delete()
        return redirect(request.POST.get('next', 'mensajes_recibidos'))#redirigir a la pagina de mensajes recibidos
    return render(request, "mensajes/eliminar_mensaje.html", {"mensaje" : mensaje, "next": request.GET.get('next', 'mensajes_recibidos')})

def home(request):
    return render(request,'home.html')

def registro(request):
    if request.method=='POST':
        form=RegistroForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            return redirect('home')
    else:
        form=RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})