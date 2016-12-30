from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from accounts.forms import UserForm


def user_create(request):
    user = User()
    if request.method == 'POST':
        form = UserForm(request.POST, instance = user)
        if form.is_valid():
            user = User.objects.create_user(request.POST.get('username'), None, request.POST.get('password'))
            user.save()
            return redirect('login')
    else:
        form = UserForm(instance=user)
    return render(request, 'accounts/register.html', dict(form = form))
