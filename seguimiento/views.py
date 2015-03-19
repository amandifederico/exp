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

def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))


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

