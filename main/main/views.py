from django.http import HttpRequest, HttpResponse
from django.template import loader
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render()) 