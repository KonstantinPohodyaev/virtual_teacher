from django.shortcuts import render


def page_not_found(request, exception):
    return render(request, 'tools/404.html', status=404)


def server_error(request):
    return render(request, 'tools/500.html', status=500)


def csrf_failure(request, reason=''):
    return render(request, 'tools/403_csrf_failure.html', status=403)
