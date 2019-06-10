from django.shortcuts import render
from django.http  import HttpResponse
from .forms import UserForm
from .models import User

# Create your views here.
def welcome(request):
    return render(request ,'index.html')

def add(request):
    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES,instance = user)
        if form.is_valid():
            user = form.save(commit=False)
            # profile.user = current_user
            user.save()
        return redirect ('/')
    else:
        form = UserForm()
   
    return render(request,'add.html',{"form":form})