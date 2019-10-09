# Create your views here.
from django.conf import settings
from django.shortcuts import render, redirect

from . forms import RegisterForm,LoginForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash




# Create your views here.




def register(request):

    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")

        newUser = User(username =username, email= email)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,"Enregistré avec succès ...")

        return redirect("accueil")
    context = {
            "form" : form
        }
    return render(request,"register.html",context)

    
    
def loginUser(request):
    form = LoginForm(request.POST or None)

    context = {
        "form":form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None:
            messages.info(request,"Nom d'utilisateur ou mot de passe incorrect")
            return render(request,"login.html",context)

        messages.success(request,"Vous vous êtes connecté(e) avec succès")
        context=("bonjour je suis connecté")
        login(request,user)
        return redirect("accueil")
        return redirect('%s?next=%s' % (settings.LOGIN_REDIRECT_URL, request.path))
    return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Vous vous êtes déconnecté(e) avec succès")
    return redirect("accueil")


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Votre mot de pase a été modifié avec succès!')
            return redirect('accueil')
        else:
            messages.error(request, "Merci de corriger l'erreur.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })