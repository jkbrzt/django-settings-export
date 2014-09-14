from django.shortcuts import render


def render_ok(request):
    return render(request, 'ok.html')


def render_error(request):
    return render(request, 'error.html')
