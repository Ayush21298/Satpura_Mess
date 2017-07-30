from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mess/index.html',{});

def queries(request):
    return render(request,'mess/queries.html',{});

def health(request):
    return render(request,'mess/health.html',{});
