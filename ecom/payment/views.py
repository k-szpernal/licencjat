from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from koszyk.koszyk import Koszyk
from payment.forms import ShippingForm, PaymentForm
from payment.models import AdresWysylki, Zamowienia, ZamowieniaProdukty
from sklep.models import Produkt, Profil
import datetime


def orders(request, pk):
    if request.user.is_authenticated and request.user.is_superuser:
        zamowienie = Zamowienia.objects.get(id=pk)
        items = ZamowieniaProdukty.objects.filter(zamowienie=pk)

        if request.POST:
            status = request.POST['shipping_status']
            if status == "true":
                zamowienie.wyslane = True
                zamowienie.save()
            else:
                zamowienie.wyslane = False
                zamowienie.save()
            messages.success(request, "Status wysyłki zaktualizowany")
            return redirect('home')

        return render(request, 'payment/orders.html',
                      {"zamowienie": zamowienie, "items": items})
    else:
        messages.success(request, "Odmowa dostępu")
        return redirect('home')



def not_shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        zamowienia = Zamowienia.objects.filter(wyslane=False)
        if request.POST:
            num = request.POST['num']
            zamowienie = Zamowienia.objects.get(id=num)
            zamowienie.wyslane = True
            zamowienie.save()
            messages.success(request, "Status wysyłki zaktualizowany")
            return redirect('home')
        return render(request, "payment/not_shipped_dash.html",
                      {"zamowienia": zamowienia})
    else:
        messages.success(request, "Odmowa dostępu")
        return redirect('home')


def shipped_dash(request):
    if request.user.is_authenticated and request.user.is_superuser:
        zamowienia = Zamowienia.objects.filter(wyslane=True)
        if request.POST:
            num = request.POST['num']
            zamowienie = Zamowienia.objects.get(id=num)
            zamowienie.wyslane = False
            zamowienie.save()
            messages.success(request, "Status wysyłki zaktualizowany")
            return redirect('home')
        return render(request, "payment/shipped_dash.html",
                      {"zamowienia": zamowienia})
    else:
        messages.success(request, "Odmowa dostępu")
        return redirect('home')

def process_order(request):
	if request.POST:
		koszyk = Koszyk(request)
		koszyk_produkty = koszyk.get_prod
		quantities = koszyk.get_quants
		totals = koszyk.cart_total()

		#pobiera dane rozliczeniowe
		payment_form = PaymentForm(request.POST or None)
		#pobiera dane wysyłki
		my_shipping = request.session.get('my_shipping')

		full_name = my_shipping['wysylka_imie_nazwisko']
		email = my_shipping['wysylka_email']
		shipping_address = f"{my_shipping['wysylka_adres1']}\n{my_shipping['wysylka_adres2']}\n{my_shipping['wysylka_miasto']}\n{my_shipping['wysylka_wojewodztwo']}\n{my_shipping['wysylka_kod_pocztowy']}\n{my_shipping['wysylka_kraj']}"
		amount_paid = totals

		#tworzy zamówienie

		if request.user.is_authenticated:
			user = request.user

			create_order = Zamowienia(uzytkownik=user, imie_nazwisko=full_name, email=email, wysylka_adres=shipping_address, koszt=amount_paid)
			create_order.save()

			#dodawanie produktów zamówienia
			#pobiera id zamówienia
			order_id = create_order.pk

			#pobiera id produktu
			for produkt in koszyk_produkty():
				product_id = produkt.id
				#pobiera cenę
				if produkt.czy_promocja:
					price = produkt.promocja_cena
				else:
					price = produkt.cena
				#ilość produktów
				for key,value in quantities().items():
					if int(key) == produkt.id:
						create_order_item = ZamowieniaProdukty(zamowienie_id=order_id, produkt_id=product_id, uzytkownik=user, ilosc=value, cena=price)
						create_order_item.save()
				#czyści koszyk
			for key in list(request.session.keys()):
				if key == "session_key":
					#Usuwa klucz sesji
					del request.session[key]
			#czyści koszyk w bazie danych
			current_user = Profil.objects.filter(uzytkownik__id=request.user.id)
			#usuwa pole 'koszyk_old'
			current_user.update(koszyk_old="")


			messages.success(request, "Zamówienie złożone")
			return redirect('home')
		else:
			#użytkownik nie zalogowany
			create_order = Zamowienia(imie_nazwisko=full_name, email=email, wysylka_adres=shipping_address, koszt=amount_paid)
			create_order.save()

			#dodawanie produktów zamówienia
			#pobiera id zamówienia
			order_id = create_order.pk

			#pobiera id produktu
			for produkt in koszyk_produkty():
				product_id = produkt.id
				#pobiera cenę
				if produkt.czy_promocja:
					price = produkt.promocja_cena
				else:
					price = produkt.cena
				#ilość produktów
				for key,value in quantities().items():
					if int(key) == produkt.id:
						create_order_item = ZamowieniaProdukty(zamowienie_id=order_id, produkt_id=product_id, ilosc=value, cena=price)
						create_order_item.save()
			#czyści koszyk w sesji
			for key in list(request.session.keys()):
				if key == "session_key":
					#Usuwa klucz sesji
					del request.session[key]
			
			messages.success(request, "Zamówienie złożone")
			return redirect('home')

	else:
		messages.success(request, "Odmowa dostępu")
		return redirect('home')

def payment_success(request):
	return render(request, "payment/payment_success.html", {})


def billing_info(request):
	if request.POST:

		koszyk = Koszyk(request)
		koszyk_produkty = koszyk.get_prod
		quantities = koszyk.get_quants
		totals = koszyk.cart_total()

		#tworzy sesję z danymi wysyłki
		my_shipping = request.POST
		request.session['my_shipping'] = my_shipping

		#użytkownik zalogowany
		if request.user.is_authenticated:
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})
		#użytkownik nie zalogowany
		else:
			billing_form = PaymentForm()
			return render(request, "payment/billing_info.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals, "shipping_info":request.POST, "billing_form":billing_form})

		shipping_form = request.POST

		return render(request, "payment/billing_info.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
	else:
		messages.success(request,"Odmowa dostępu")
		return redirect('home')


def checkout(request):
	koszyk = Koszyk(request)
	koszyk_produkty = koszyk.get_prod
	quantities = koszyk.get_quants
	totals = koszyk.cart_total()

	if request.user.is_authenticated:
		#jako zalogowany użytkownik
		shipping_user = AdresWysylki.objects.get(uzytkownik__id=request.user.id)
		shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
		return render(request, "payment/checkout.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})
	else:
		#jako gość
		shipping_form = ShippingForm(request.POST or None)
		return render(request, "payment/checkout.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals, "shipping_form":shipping_form})