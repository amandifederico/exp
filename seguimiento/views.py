# -*- coding: utf-8 -*-

#--PDF----------------------------------------------------
"""import ho.pisa as pisa #esto hay que bajarlo de internet, se puede instalar con easy install - http://pypi.python.org/pypi/pisa/
import cStringIO as StringIO
import cgi
from django.template.loader import *"""
#--PDF----------------------------------------------------

from seguimiento.models import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext, Template, Context
from django.http import HttpResponseRedirect, HttpResponse
#---LOGOUT---
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.template.response import TemplateResponse
#---LOGOUT---
# Create your views here.
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from datetime import *

#--------------------------------
#def generar_pdf(html):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
#    result = StringIO.StringIO()
#    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
#    if not pdf.err:
#        return HttpResponse(result.getvalue(), mimetype='application/pdf')
#    return HttpResponse('Error al generar el PDF: %s' % cgi.escape(html))
"""
def generar_pdf_completo(html,nomb,id,fecha):
    # Función para generar el archivo PDF y devolverlo mediante HttpResponse
    result = StringIO.StringIO()

    pisa.CreatePDF(html,result)
#    pdf = pisa.pisaDocument(StringIO.StringIO(html.encode("UTF-8")), result)
    response = HttpResponse(result.getvalue(), mimetype ='application/pdf')
    response['Content-Disposition'] = 'attachment; filename='+nomb+'-'+str(id)+'-'+str(fecha)+'.pdf'
    return response
"""

#--------------------------------
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

#////////////////////////////////////////////////////////////////////////////////////////

#LISTADOS
def estadisticas(request):
    usr = User.objects.exclude(username = 'admin')
    return render_to_response('estadisticas.html',context_instance=RequestContext(request,{'usr':usr},))

def listados(request):
    usr = User.objects.exclude(username = 'admin')

    return render_to_response('listados.html',context_instance=RequestContext(request,{'usr':usr},))

def listDocs(request):
    doc = Documento.objects.all()
    lista = paginar(doc,request)
    """
    html = render_to_string('documentos.html', {'pagesize':'A4', 'lista':lista},context_instance=RequestContext(request))
    return generar_pdf_completo(html,'Documentos',0,datetime.now())
    """
    return render_to_response('documentos.html',context_instance=RequestContext(request,{'lista':lista},))

def listDocsUsr(request, usr):
    doc = Documento.objects.filter(recepcion = int(usr))
    lista = paginar(doc,request)
    return render_to_response('documentos.html',context_instance=RequestContext(request,{'lista':lista},))
    
def listDocsFecha(request,d1,m1,a1,d2,m2,a2,opc):
    fecha1 = datetime(int(a1),int(m1),int(d1))
    fecha2 = datetime(int(a2),int(m2),int(d2))
    if int(opc) == 1:
        doc = Documento.objects.filter(fecha_ing__range = (fecha1,fecha2))
        lista = paginar(doc,request)
        return render_to_response('documentos.html',context_instance=RequestContext(request,{'lista':lista},))
    elif int(opc) == 2:
        pas = Pase.objects.filter(fecha_ing__range = (fecha1,fecha2))
        lista = paginar(pas,request)
        return render_to_response('pase.html',context_instance=RequestContext(request,{'lista':lista},))

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

