from django.shortcuts import render

def homepage(request):
    if request.method=='POST':
        password=request.get['name']
    return render(request,"pssd\index.html")