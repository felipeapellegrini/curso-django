from django.http import HttpResponse


def home(request):
    return HttpResponse('<html><body>Olá mundo</body></html>', content_type='text/html')
