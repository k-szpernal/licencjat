from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import datetime

class Profil(models.Model):
	uzytkownik = models.OneToOneField(User, on_delete=models.CASCADE)
	data_modyfikacji = models.DateTimeField(User, auto_now=True)
	telefon = models.CharField(max_length=15, blank=True)
	adres1 = models.CharField(max_length=150, blank=True)
	adres2 = models.CharField(max_length=150, blank=True)
	miasto = models.CharField(max_length=60, blank=True)
	wojewodztwo = models.CharField(max_length=40, blank=True)
	kod_pocztowy = models.CharField(max_length=15, blank=True)
	kraj = models.CharField(max_length=40, blank=True)
	koszyk_old = models.CharField(max_length=200, blank=True, null=True)

	def __str__(self):
		return self.uzytkownik.username

	class Meta:
		verbose_name ='Profil'
		verbose_name_plural = 'Profile'
# tworzy Profil w momencie rejestracji
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profil(uzytkownik=instance)
		user_profile.save()
#automatyzacja
post_save.connect(create_profile, sender=User)

class Kategoria(models.Model):
	nazwa = models.CharField(max_length=50)

	def __str__(self):
		return self.nazwa

	class Meta:
		verbose_name ='Kategoria'
		verbose_name_plural = 'Kategorie'

class Klient(models.Model):
	imie = models.CharField(max_length=50)
	nazwisko = models.CharField(max_length=50)
	telefon = models.CharField(max_length=15)
	email = models.EmailField(max_length=250)
	haslo = models.CharField(max_length=50)


	def __str__(self):
		return f'{self.imie} {self.nazwisko}'

	class Meta:
		verbose_name_plural = 'Klienci'

class Produkt(models.Model):
	nazwa = models.CharField(max_length=100)
	cena = models.DecimalField(default=0, decimal_places=2, max_digits=6)
	kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, default=1)
	opis = models.CharField(max_length=250, default='', blank=True, null=True)
	zdjecie = models.ImageField(upload_to='uploads/product/')
	# Promocje
	czy_promocja = models.BooleanField(default=False, null=True)
	promocja_cena = models.DecimalField(default=0, decimal_places=2, max_digits=6, null=True)

	def __str__(self):
		return self.nazwa

	class Meta:
		verbose_name_plural = 'Produkty'

class Zamowienia(models.Model):
	produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
	klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
	ilosc = models.IntegerField(default=1)
	adres = models.CharField(max_length=150, default='', blank=True)
	telefon = models.CharField(max_length=15, default='', blank=True)
	data = models.DateField(default=datetime.datetime.today)
	status = models.BooleanField(default=False)

	def __str__(self):
		return self.produkt

	class Meta:
		verbose_name_plural = 'Zamowienia'
