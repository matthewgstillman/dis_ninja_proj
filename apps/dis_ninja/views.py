from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    print "no ninjas here"
    return render(request, 'dis_ninja/index.html')

def ninjas(request):
    context = {
        'src': "../static/img/ninjas/tmnt.png"
    }
    return render(request, 'dis_ninja/ninjas.html', context)

def check_colors(request, color):

    if color == 'purple':
        src ="../static/img/ninjas/donatello.jpg"
    elif color == 'red':
        src ="../static/img/ninjas/raphael.jpg"
    elif color == 'orange':
        src ="../static/img/ninjas/michelangelo.jpg"
    elif color == 'blue':
        src ="../static/img/ninjas/leonardo.jpg"
    else:
        src = "../static/img/ninjas/notapril.jpg"
    context = {
        'src': src
    }
    return render(request, 'dis_ninja/ninjas.html', context)
