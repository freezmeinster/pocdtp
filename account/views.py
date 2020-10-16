from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from account.libs import decrypt
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/dashboard/")
    if request.method == "POST":
        token = request.POST.get("csrfmiddlewaretoken")[0:20]
        enc_user = request.POST.get("username")
        enc_pass = request.POST.get("password")
        raw_user = decrypt(enc_user, token)
        raw_pass = decrypt(enc_pass, token)
        user = authenticate(username=raw_user, password=raw_pass)
        if user is not None:
            login(request, user)
            return JsonResponse({"url": "/dashboard/"})
        else:
            return JsonResponse({"url": "/"}, status=403)
    return render(request, "account/index.html", locals())

@login_required
def dashboard(request):
    return render(request, "account/dashboard.html")
