from django.contrib import admin
from django.contrib.auth.models import User
from .models import Kategoria, Klient, Produkt, Zamowienia, Profil

admin.site.register(Kategoria)
admin.site.register(Klient)
admin.site.register(Produkt)
admin.site.register(Zamowienia)
admin.site.register(Profil)


class ProfileInline(admin.StackedInline):
	model = Profil

#rozszerzenie modelu użytkownika
class UserAdmin(admin.ModelAdmin):
	model = User
	field = ["username", "first_name", "last_name", "email"]
	inlines = [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
