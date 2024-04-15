from django.shortcuts import render

# Create your views here.


def shortener_link(request):
    if request.method == 'GET':
        return render(request, 'short_link.html')


def shortened_link(request):
    if request.method == 'GET':
        return render(request, 'shortened_link.html')
