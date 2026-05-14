from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request):
    return render(request, "web3Svarog/index.html")

def leistungen(request):
    return render(request, "web3Svarog/leistungen.html")

def projekte(request):
    return render(request, "web3Svarog/projekte.html")

def datenschutz(request):
    return render(request, "web3Svarog/datenschutz.html")

def impressum(request):
    return render(request, "web3Svarog/impressum.html")

def kontakt(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        full_message = f"""
        Neue Nachricht von: {name}
        Email: {email}

        Nachricht:
        {message}
        """

        send_mail(
            subject="Neue Kontaktanfrage - 3Svarog",
            message=full_message,
            from_email="noreply@3svarog.com",
            recipient_list=["info@firma.de"],
        )

        messages.success(request, "Nachricht wurde gesendet!")
        return redirect("kontakt")

    return render(request, "web3Svarog/kontakt.html")
