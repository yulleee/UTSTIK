from django.shortcuts import render

# Create your views here.
def mtk(request):
    return render(request, 'index.html')