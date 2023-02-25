from django.shortcuts import render

def homepage(request):
    if request.method=='POST':
        password=request.method['pass']
        print(password)
    return render(request,"pssdgen\index.html")