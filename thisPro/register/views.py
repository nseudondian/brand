from django.shortcuts import render, redirect
from django.contrib import messages
from .form import NewForm




def register(request):
    if request.method == 'POST':
        form = NewForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('home')
    else:
        form = NewForm()
    
    return render(request, "register/form.html", {'form':form})
