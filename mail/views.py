from django.shortcuts import render,get_object_or_404,redirect
from django.http  import HttpResponse
from .forms import UserForm
from .models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# Create your views here.
def welcome(request):
    return render(request ,'index.html')

def add(request):
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            context = {
				user.First_Name:'first_name',
				user.Last_Name:'last_name',
				user.Email:'email',
			}
            return redirect ('list.html',context)
    else:
        form = UserForm()
   
    return render(request,'add.html',{"form":form})




def directory(request):

    lists = User.objects.all().reverse()
    return render(request,'list.html',{"lists":lists})

