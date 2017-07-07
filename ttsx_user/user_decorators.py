from django.shortcuts import redirect


def user_islogin(func):

    def innner(request, *args, **kwargs):
        if request.session.has_key('uid'):
            return func(request, *args, **kwargs)
        else:
            return redirect('/user/login/')
    return innner