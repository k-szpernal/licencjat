import datetime
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from sklep.models import Produkt

class AdresWysylki(models.Model):
	uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	wysylka_imie_nazwisko = models.CharField(max_length=150, null=True)
	wysylka_email = models.CharField(max_length=250)
	wysylka_adres1 = models.CharField(max_length=150)
	wysylka_adres2 = models.CharField(max_length=150, null=True, blank=True)
	wysylka_miasto = models.CharField(max_length=60)
	wysylka_wojewodztwo = models.CharField(max_length=40, null=True, blank=True)
	wysylka_kod_pocztowy = models.CharField(max_length=15)
	wysylka_kraj = models.CharField(max_length=40)


	class Meta:
		verbose_name_plural = "Adres Wysylki"

	def __str__(self):
		return f'Adres Wysylki - {str(self.id)}'

#tworzy adres wysyłki w momencie rejestracji
def create_shipping(sender, instance, created, **kwargs):
	if created:
		user_shipping = AdresWysylki(uzytkownik=instance)
		user_shipping.save()
#automatyzacja
post_save.connect(create_shipping, sender=User)


class Zamowienia(models.Model):
	uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	imie_nazwisko = models.CharField(max_length=150, null=True)
	email = models.EmailField(max_length=250)
	wysylka_adres = models.TextField(max_length=10000)
	koszt = models.DecimalField(max_digits=8, decimal_places=2)
	data_zamowienia = models.DateTimeField(auto_now_add=True)
	wyslane = models.BooleanField(default=False)
	data_wyslania = models.DateTimeField(blank=True, null=True)

	class Meta:
		verbose_name_plural = "Zamowienia"

	def __str__(self):
		return f'Zamowienie - {str(self.id)}'

#Automatyczne dodawanie daty wysłania
@receiver(pre_save, sender=Zamowienia)
def set_shipped_date_on_update(sender, instance, **kwargs):
    if instance.pk:
        obj = sender._default_manager.get(pk=instance.pk)
        if instance.wyslane and not obj.wyslane:
            instance.data_wyslania = datetime.datetime.now()
        elif not instance.wyslane and obj.wyslane:
            instance.data_wyslania = None


class ZamowieniaProdukty(models.Model):
	zamowienie = models.ForeignKey(Zamowienia, on_delete=models.CASCADE, null=True)
	produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE, null=True)
	uzytkownik = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	ilosc = models.PositiveBigIntegerField(default=1)
	cena = models.DecimalField(max_digits=8, decimal_places=2)

	class Meta:
		verbose_name_plural = "Zamowienia Produkty"

	def __str__(self):
		return f'Zamowione produkty - {str(self.id)}'
