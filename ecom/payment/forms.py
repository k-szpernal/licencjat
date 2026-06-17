from django import forms
from .models import AdresWysylki

class ShippingForm(forms.ModelForm):
	wysylka_imie_nazwisko = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię i nazwisko'}), required=True)
	wysylka_email = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres Email'}), required=True)
	wysylka_adres1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres1'}), required=True)
	wysylka_adres2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres2'}), required=False)
	wysylka_miasto = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Miejscowość'}), required=True)
	wysylka_wojewodztwo = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Województwo'}), required=False)
	wysylka_kod_pocztowy = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kod pocztowy'}), required=True)
	wysylka_kraj = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kraj'}), required=True)

	class Meta:
		model = AdresWysylki
		fields = ['wysylka_imie_nazwisko', 'wysylka_email', 'wysylka_adres1', 'wysylka_adres2', 'wysylka_miasto', 'wysylka_wojewodztwo', 'wysylka_kod_pocztowy', 'wysylka_kraj']

		exclude = ['uzytkownik',]



class PaymentForm(forms.Form):
	card_name = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię i nazwisko'}), required=True)
	card_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numer karty'}), required=True)
	card_exp_date = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Data ważności karty'}), required=True)
	card_cvv_number = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kod CVC/CVV'}), required=True)
	card_address1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres rozliczeniowy 1'}), required=True)
	card_address2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres rozliczeniowy 2'}), required=False)
	card_city = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Miejscowość'}), required=True)
	card_province = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Województwo'}), required=True)
	card_zipcode = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kod pocztowy'}), required=True)
	card_country = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kraj'}), required=True)
