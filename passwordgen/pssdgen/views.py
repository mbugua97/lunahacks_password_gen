from django.shortcuts import render

def homepage(request):
    if request.method=='POST':
        password=request.POST['pass']
        print(password)
    return render(request,"pssdgen\index.html")