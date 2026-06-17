from django.contrib import admin
from django.contrib.auth.models import User
from .models import AdresWysylki, Zamowienia, ZamowieniaProdukty

admin.site.register(AdresWysylki)
admin.site.register(Zamowienia)
admin.site.register(ZamowieniaProdukty)

#złączenie zamówień z produktami
class OrderItemInline(admin.StackedInline):
	model = ZamowieniaProdukty
	extra = 0


class OrderAdmin(admin.ModelAdmin):
	model= Zamowienia
	inlines = [OrderItemInline]
	readonly_fields = ["data_zamowienia"]
	fields = ["uzytkownik", "imie_nazwisko", "email", "wysylka_adres", "koszt", "data_zamowienia", "wyslane", "data_wyslania"]

admin.site.unregister(Zamowienia)

admin.site.register(Zamowienia, OrderAdmin)