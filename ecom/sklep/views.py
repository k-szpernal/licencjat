from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
import json
from koszyk.koszyk import Koszyk
from .forms import SignUpForm, UpdateForm, ChangePassForm, UserInfoForm
from payment.forms import ShippingForm
from payment.models import AdresWysylki
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Produkt, Kategoria, Profil

def home(request):
	produkty = Produkt.objects.all()
	return render(request, 'home.html', {'produkty':produkty})

def search(request):
	if request.method == "POST":
		searched = request.POST['searched']
		#wysyła zapytanie do bazy
		searched = Produkt.objects.filter(Q(nazwa__icontains=searched) | Q(opis__icontains=searched)) #icontains pozwala wyszukiwać niezależnie od wielkości liter
		if not searched:
			messages.success(request, "Taki produkt nie istnieje.")
			return render(request, "search.html", {})
		else:
			return render(request, "search.html", {'searched':searched})
	else:
		return render(request, "search.html", {})

def update_info(request):
	if request.user.is_authenticated:
		#pobiera użytkownika
		current_user = Profil.objects.get(uzytkownik__id=request.user.id)
		#pobiera informacje do wysyłki
		shipping_user = AdresWysylki.objects.get(uzytkownik__id=request.user.id)
		form = UserInfoForm(request.POST or None, instance=current_user)
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

		if form.is_valid() and shipping_form.is_valid():
			form.save()
			shipping_form.save()

			messages.success(request, "Dane zostały zaktualizowane!")
			return redirect('home')
		return render(request, "update_info.html", {'form':form, 'shipping_form':shipping_form})
	else:
		messages.success(request, "Zaloguj się aby edytować swoje dane.")
		return redirect('home')



def update_password(request):
	if request.user.is_authenticated:
		current_user = request.user
		#sprawdzenie czy formularz jest wypełniony
		if request.method == 'POST':
			form = ChangePassForm(current_user, request.POST)
			#czy jest poprawnie wypełniony
			if form.is_valid():
				form.save()
				messages.success(request, "Twoje hasło zostało zmienione.")
				login(request, current_user)
				return redirect('update_user')
			else:
				for error in list(form.errors.values()):
					messages.error(request, error)
					return redirect('update_password')
		else:
			form = ChangePassForm(current_user)
			return render(request, "update_password.html", {'form':form})
	else:
		messages.success(request, "Zaloguj się aby zmienić hasło.")
		return redirect('home')


def register_user(request):
	form = SignUpForm()
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate (username=username, password=password)
			login(request, user)
			messages.success(request, ("Rejestracja przebiegła pomyślnie! Poniżej możesz wypełnić swoje dane."))
			return redirect('update_info')
		else:
			messages.success(request, ("Wystąpił błąd podczas rejestacji. Proszę spróbuj ponownie."))
			return redirect('register')
	else:
		return render(request, 'register.html', {'form':form})




def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			#sekcja kodu do zapisu koszyka w sesji konta
			current_user = Profil.objects.get(uzytkownik__id=request.user.id)
			saved_cart = current_user.koszyk_old
			if saved_cart:
				#zamiana na słownik python przy użyciu JSON
				converted_cart = json.loads(saved_cart)
				#dodanie słownika do sesji
				koszyk = Koszyk(request)
				for key,value in converted_cart.items():
					koszyk.db_add(produkt=key, ilosc=value)
			messages.success(request, ("Pomyślnie zalogowano!"))
			return redirect('home')
		else:
			messages.success(request, ("Uwierzytelnienie nie powiodło się, spróbuj ponownie."))
			return redirect('login')
	else:
		return render(request, 'login.html', {})

def update_user(request):
	if request.user.is_authenticated:
		current_user = User.objects.get(id=request.user.id)
		user_form = UpdateForm(request.POST or None, instance=current_user)

		if user_form.is_valid():
			user_form.save()

			login(request, current_user)
			messages.success(request, "Pomyślnie zmieniono dane użytkownika!")
			return redirect('home')
		return render(request, "update_user.html", {'user_form':user_form})
	else:
		messages.success(request, "Zaloguj się aby edytować swój profil.")
		return redirect('home')

def logout_user(request):
	logout(request)
	messages.success(request, ("Wylogowano pomyślnie!"))
	return redirect('home')


def about(request):
	return render(request, 'about.html', {})


def product(request,pk):
	produkt = Produkt.objects.get(id=pk)
	return render(request, 'product.html', {'produkt':produkt})

def category_summary(request):
	kategorie = Kategoria.objects.all()
	return render(request, 'category_summary.html', {"kategorie":kategorie})


def category(request, kat):
    kat = kat.replace('-', ' ')
    try:
        kategoria = Kategoria.objects.get(nazwa=kat)
        produkty = Produkt.objects.filter(kategoria=kategoria)
        return render(request, 'category.html', {'produkty': produkty, 'kategoria': kategoria})
    except:
        messages.success(request, ("Taka kategoria nie istnieje"))
        return redirect('home')