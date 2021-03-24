from django.shortcuts import render


def mainHome(request):
    context={}
    return render(request, 'main.html', context)