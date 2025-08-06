from django.shortcuts import render, get_object_or_404, redirect
from django.core.mail import send_mail
from django.conf import settings
from .models import Contacto
from .forms import FormularioContacto



def lista_contacto(request):

    todos_los_contactos = Contacto.objects.all().order_by('pk')

    contacto_principal = todos_los_contactos.first()

    colectividades = todos_los_contactos.exclude(pk=contacto_principal.pk)


    if request.method == 'POST':
        form = FormularioContacto(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            email_remitente = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            mensaje_completo = f"De: {nombre} ({email_remitente})\n\n{mensaje}"

            send_mail(
                subject=asunto,
                message=mensaje_completo,
                from_email=settings.EMAIL_HOTS_USER,
                recipient_list=[contacto_principal.email_1],
                fail_silently=False,

            )
            return redirect('contacto:path_contacto_main')
    else:
        form = FormularioContacto()

    contexto = {
        'contacto_principal': contacto_principal,
        'colectividades': colectividades,
        'form': form,

    }

    return render(request, 'contacto/contacto_main.html', contexto)


