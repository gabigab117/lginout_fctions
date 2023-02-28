from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegistrationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login as log_user
from django.contrib.auth import logout as logout_user

# on utilise 3 fonctions pour login/out fondées sur les fonctions : authenticate / login / logout


def home(request):
    return HttpResponse(f"Bienvenu {request.user}")


def signup(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "accounts/signup.html", {"form": form})


def login(request):
    if request.method == "POST":
        # name du formulaire = username et password
        username = request.POST.get("username")
        password = request.POST.get("password")
        # si username et password correspondent la variable user correspond à CustomUser
        user = authenticate(request, username=username, password=password)
        # si l'user a été correctement authentifié ==>
        if user is not None:
            # on le connecte
            log_user(request, user)
            return redirect("home")
        else:
            return HttpResponse("Impossible de connecter l'utilisateur")

    return render(request, 'registration/login.html', {})


def logout(request):
    logout_user(request)
    return redirect("home")
