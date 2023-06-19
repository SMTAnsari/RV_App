from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper(request, *arg, **kwargs):
        if not request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request, *arg, **kwargs)
    return wrapper