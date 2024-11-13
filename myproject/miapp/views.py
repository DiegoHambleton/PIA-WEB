from django.shortcuts import render, redirect
from .forms import RespuestaFormularioForm
from .forms import ContactForm

def home(request):
    return render(request, 'index.html')

def form_view(request):
    if request.method == 'POST':
        form = RespuestaFormularioForm(request.POST)
        if form.is_valid():
            # Aquí procesas los datos
            return render(request, 'formsexito/form_success.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'form.html', {'form': form})

def home(request):
    return render(request, 'index.html')

def pagina2(request):
    return render(request, 'pagina2.html')

def pagina3(request):
    return render(request, 'pagina3.html')

def pagina4(request):
    return render(request, 'pagina4.html')

def pagina5(request):
    return render(request, 'pagina5.html')