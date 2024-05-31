from django.shortcuts import render
from django.http import HttpResponse
from demo.fm_init import flags
from django.template import loader

def index(request):
    response = "Hello, world. You're at the polls index."
    template = loader.get_template('template.html')
    context = {'flags': {
        'message': flags.message.get_value(),
        'fontColor': flags.fontColor.get_value(),
        'fontSize': flags.fontSize.get_value(),
        'showMessage': flags.showMessage.get_value(),
    }}
    return HttpResponse(template.render(context, request))