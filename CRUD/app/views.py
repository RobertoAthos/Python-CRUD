from .models import User
from django.shortcuts import redirect, render
from .forms import UserForm

# Create your views here.

def index(req):
    users = User.objects.all()
    context ={
        'users': users
    }
    return render(req,'users/index.html', context)

def create(req):
    if req.method == 'GET':
        form = UserForm
        context = {
        'form': form
        }
        return render(req, 'users/create.html', context=context)
    else:
        form = UserForm(req.POST)
        if form.is_valid():
           form.save()
           return redirect(index)

def edit(req, user_id):
    user = User.objects.get(pk = user_id)
    if req.method == 'POST':
        form = UserForm(data=req.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect(index)
    else:
        form = UserForm(instance=user)
        context = {'form': form}
        return render(req, 'users/create.html', context=context)
    

def delete(req, user_id):
    user = User.objects.get(pk = user_id)
    user.delete()
    return redirect(index)
