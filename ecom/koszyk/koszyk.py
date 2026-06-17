from sklep.models import Produkt, Profil

class Koszyk():
	def __init__(self, request):
		self.session = request.session

		self.request = request
		#pobiera klucz sesji
		koszyk = self.session.get('session_key')
		#tworzy nowy klucz w przypadku nowego użytkownika
		if 'session_key' not in request.session:
			koszyk = self.session['session_key'] = {}



		self.koszyk = koszyk

	def db_add(self, produkt, ilosc):
		produkt_id = str(produkt)
		product_qty = str(ilosc)
		if produkt_id in self.koszyk:
			pass
		else:
			#self.koszyk[produkt_id] = {'cena': str(produkt.cena)}
			self.koszyk[produkt_id] = int(product_qty)

		self.session.modified = True

		#przypadek gdy użytkownik jest zalogowany
		if self.request.user.is_authenticated:
			#pobiera profil użytkownika
			current_user = Profil.objects.filter(uzytkownik__id=self.request.user.id)
			#zamiana znaków ze słownika python aby dane były czytelne dla JSON
			koszyczek = str(self.koszyk)
			koszyczek = koszyczek.replace("\'", "\"")
			#zapis do modelu Profil
			current_user.update(koszyk_old=str(koszyczek))

	def add(self, produkt, ilosc):
		produkt_id = str(produkt.id)
		product_qty = str(ilosc)
		if produkt_id in self.koszyk:
			pass
		else:
			#self.koszyk[produkt_id] = {'cena': str(produkt.cena)}
			self.koszyk[produkt_id] = int(product_qty)

		self.session.modified = True

		#przypadek gdy użytkownik jest zalogowany
		if self.request.user.is_authenticated:
			#pobiera profil użytkownika
			current_user = Profil.objects.filter(uzytkownik__id=self.request.user.id)
			#zamiana znaków ze słownika python aby dane były czytelne dla JSON
			koszyczek = str(self.koszyk)
			koszyczek = koszyczek.replace("\'", "\"")
			#zapis do modelu Profil
			current_user.update(koszyk_old=str(koszyczek))



	def __len__(self):
		return len(self.koszyk)


	def get_prod(self):
		produkt_ids = self.koszyk.keys()
		produkty = Produkt.objects.filter(id__in=produkt_ids)

		return produkty

	def get_quants(self):
		quantities = self.koszyk
		return quantities

	def delete(self, produkt):
		produkt_id = str(produkt)
		#usuń z koszyka
		if produkt_id in self.koszyk:
			del self.koszyk[produkt_id]
		self.session.modified = True

		#przypadek gdy użytkownik jest zalogowany
		if self.request.user.is_authenticated:
			#pobiera profil użytkownika
			current_user = Profil.objects.filter(uzytkownik__id=self.request.user.id)
			#zamiana znaków ze słownika python aby dane były czytelne dla JSON
			koszyczek = str(self.koszyk)
			koszyczek = koszyczek.replace("\'", "\"")
			#zapis do modelu Profil
			current_user.update(koszyk_old=str(koszyczek))

	def update(self, produkt, ilosc):
		produkt_id = str(produkt)
		product_qty = int(ilosc)

		nkoszyk = self.koszyk

		nkoszyk[produkt_id] = product_qty

		self.session.modified = True


		if self.request.user.is_authenticated:
			#pobiera profil użytkownika
			current_user = Profil.objects.filter(uzytkownik__id=self.request.user.id)
			#zamiana znaków ze słownika python aby dane były czytelne dla JSON
			koszyczek = str(self.koszyk)
			koszyczek = koszyczek.replace("\'", "\"")
			#zapis do modelu Profil
			current_user.update(koszyk_old=str(koszyczek))
		xyz = self.koszyk
		return xyz

	def cart_total(self):
		#pobierz ID produktu
		produkt_ids = self.koszyk.keys()
		#szuka kluczy produktu w bazie
		produkty = Produkt.objects.filter(id__in=produkt_ids)
		quantities = self.koszyk
		total = 0
		for key, value in quantities.items():
			key = int(key)
			for produkt in produkty:
				if produkt.id == key:
					if produkt.czy_promocja:
						total = total + (produkt.promocja_cena * value)
					else:
						total = total + (produkt.cena * value)
		return total
