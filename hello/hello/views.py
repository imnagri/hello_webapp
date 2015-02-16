from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
from django.template import RequestContext
# from django.core.context_processors import csrf
# from django.contrib.auth.models import User

def home(request):
    args = {}
    args['name'] = 'Hussain'
    return render_to_response('htmlPage.html',args,context_instance=RequestContext(request))