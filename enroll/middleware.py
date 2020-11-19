
import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth import logout

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]


class AuthMiddleware:
    def __init__ (self,get_response):
        self.get_response = get_response
    
    def __call__(self,Request):
        response = self.get_response(Request)
        return response

    def process_view(self,Request,view_func,view_args,view_kwargs):
        assert hasattr(Request,'user')
        path = Request.path_info.lstrip('/')
        
        url_is_exempt = any(url.match(path) for url in EXEMPT_URLS)
        
        if path == reverse('logout').lstrip('/'):
            logout(Request)

        if Request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_REDIRECT_URL)
        elif Request.user.is_authenticated or url_is_exempt:
            return None
        else:
            return redirect(settings.LOGIN_URL)

        