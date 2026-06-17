from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from sklep.models import Produkt
from .koszyk import Koszyk

def cart_summary(request):
	koszyk = Koszyk(request)
	koszyk_produkty = koszyk.get_prod
	quantities = koszyk.get_quants
	totals = koszyk.cart_total()
	return render(request, "cart_summary.html", {"koszyk_produkty":koszyk_produkty, "quantities":quantities, "totals":totals})

def cart_update(request):
	koszyk = Koszyk(request)
	if request.POST.get('action') == 'post':
		#zbiera informacje
		produkt_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		koszyk.update(produkt=produkt_id, ilosc=product_qty)

		response = JsonResponse({'qty':product_qty})
		messages.success(request, ("Ilość produktów została zaktualizowana!"))
		return response
		#return redirect('cart_summary')

def cart_add(request):
	koszyk = Koszyk(request)
	if request.POST.get('action') == 'post':
		#zbiera informacje
		produkt_id = int(request.POST.get('product_id'))
		product_qty = int(request.POST.get('product_qty'))

		#szuka produktu w bazie
		produkt = get_object_or_404(Produkt, id=produkt_id)
		#zapis do sesji
		koszyk.add(produkt=produkt, ilosc=product_qty)

		koszyk_ilosc = koszyk.__len__()

		#response = JsonResponse({'Nazwa produktu: ': produkt.nazwa})
		response = JsonResponse({'ilosc': koszyk_ilosc})
		messages.success(request, ("Produkt został dodany do koszyka!"))
		return response

def cart_delete(request):
	koszyk = Koszyk(request)
	if request.POST.get('action') == 'post':
		#zbiera informacje
		produkt_id = int(request.POST.get('product_id'))
		#wywołanie funkcji delete
		koszyk.delete(produkt=produkt_id)

		response = JsonResponse({'produkt':produkt_id})
		messages.success(request, ("Produkt został usunięty z koszyka!"))
		return response
