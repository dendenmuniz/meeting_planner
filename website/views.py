from django.http import HttpResponse
from django.shortcuts import render

from meetings.models import Meeting

# Create your views here.

# 3 parametro é um dict com o conteudo que desejo mandar como parametro para o template
# conteudo dinamico


def welcome(request):
    if request.user.is_authenticated:
        context={"meetings": Meeting.objects.all()}
    else:
        context={}
    return render(request, template_name="website/welcome.html",
                  context=context)


def about(request):
    text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed id leo non sem volutpat hendrerit. Mauris tempor elementum tempus. Vestibulum ut laoreet nisi, vitae tristique leo. Curabitur hendrerit ac arcu vitae consectetur. Aliquam gravida suscipit faucibus. Aliquam malesuada enim eget mi pulvinar feugiat. Etiam molestie, enim ut scelerisque viverra, ipsum massa facilisis tortor, at tempus justo sapien at mauris. In bibendum mauris id augue rhoncus ornare. Pellentesque semper odio at tellus eleifend lacinia. Praesent ac tortor dolor. Pellentesque dui lectus, vehicula eu lorem quis, posuere vehicula nisi. Morbi metus sapien, vestibulum non fermentum ac, blandit pellentesque est."
    return HttpResponse(text)
