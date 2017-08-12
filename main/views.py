from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'mess/index.html',{});

def queries(request):
    return render(request,'mess/queries.html',{});

def health(request):
    return render(request,'mess/health.html',{});

def feedback(request):
    return render(request,'main/feedback_form.html',{});

def birthday(request):
    return render(request,'main/birthday.html',{});

def items(request):
    return render(request,'main/items.html',{});
