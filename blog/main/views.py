from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        'title':'Index Blog',
        'developer': 'Boris Isac',
        'psychologist': 'Bruieva Oksana'
    }
    return render(request, 'index.html', context)