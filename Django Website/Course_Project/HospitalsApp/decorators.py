from django.shortcuts import redirect
from django.contrib import messages

def authenticated_user(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('homepage')
        else:
            return func(request, *args, **kwargs)
    return wrapper

def allowed_user(allowed_groups=[]):
    def inner(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_groups:
                return func(request, *args, **kwargs)
            else:
                messages.error(request, ('Access Denied!'))
                return redirect('homepage')
        return wrapper
    return inner