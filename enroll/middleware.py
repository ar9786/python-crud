
import re
from django.conf import settings
from django.urls import reverse
from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth import logout



EXEMPT_URLS = settings.LOGIN_EXEMPT_URLS


class AuthMiddleware:
    def __init__ (self,get_response):
        self.get_response = get_response
    
    def __call__(self,Request):
        response = self.get_response(Request)
        return response

    def process_view(self,Request,view_func,view_args,view_kwargs):
        assert hasattr(Request,'user')
        path = Request.path_info.lstrip('/').split('/')
  
        for url in path:
            print(url)
            if(url in EXEMPT_URLS):
                url_is_exempt = 1
                break
            else:
                url_is_exempt = 0
        
        if path == reverse('logout').lstrip('/'):
            logout(Request)

        if not Request.user.is_authenticated and url_is_exempt:
            return redirect(settings.LOGIN_URL)
        else:
            return None

        