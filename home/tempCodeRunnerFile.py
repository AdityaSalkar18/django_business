from django.shortcuts import render,HttpResponse

# Create your views here.render
def index(request):
    return HttpResponse("this is homepage")