from seguimiento.models import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
#---LOGOUT---
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.template.response import TemplateResponse
#---LOGOUT---
# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def paginar(objlist,peticion):
    """Metodo que pagina el resultado de un reporte de tipo listado """
    cant = 40 #cantidad por pagina
    paginator = Paginator(objlist,cant)
    try:
        page = int(peticion.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        lista = paginator.page(page)
    except (EmptyPage, InvalidPage):
        lista = paginator.page(paginator.num_pages)
    return lista

def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def estadisticas(request):
    return render_to_response('estadisticas.html',context_instance=RequestContext(request))

#////////////////////////////////////////////////////////////////////////////////////////
#LISTADOS
def listados(request):
    return render_to_response('listados.html',context_instance=RequestContext(request))

def listDocs(request):
    doc = Documento.objects.all()
    lista = paginar(doc,request)
    return render_to_response('documentos.html',context_instance=RequestContext(request,{'lista':lista},))
    
#Por tipo de documento

#Por proveedor
#def docProv(request,idprov):
#    doc = Documento.object.filter(proveedor = idprov)
#    return render_to_response('',context_instance=RequestContext(request))
#Por usr
#def docUsr(request,idusr):
#    doc = Documento.object.filter(recepcion = idusr)
#    return render_to_response('',context_instance=RequestContext(request))


#////////////////////////////////////////////////////////////////////////////////////////
def logout(request, next_page=None, template_name='registration/logged_out.html',redirect_field_name=REDIRECT_FIELD_NAME, current_app=None, extra_context=None):
    """
    Logs out the user and displays 'You are logged out' message.
    """
    auth_logout(request)
    redirect_to = request.REQUEST.get(redirect_field_name, 'index')
    if redirect_to:
        return HttpResponseRedirect('/index')

    if next_page is None:
        current_site = 'index'
        context = {
            'site': 'index',
            'site_name': 'Inicio',
            'title': 'Usted esta saliendo...'
        }
        if extra_context is not None:
            context.update(extra_context)
        return TemplateResponse(request, template_name, context,current_app=current_app)
    else:
        # Redirect to this page until the session has been cleared.
        return HttpResponseRedirect(next_page or request.path)

