from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profil


class UserInfoForm(forms.ModelForm):
	telefon = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefon'}), required=False)
	adres1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres 1'}), required=False)
	adres2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres 2'}), required=False)
	miasto = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Miejscowość'}), required=False)
	wojewodztwo = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Województwo'}), required=False)
	kod_pocztowy = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kod pocztowy'}), required=False)
	kraj = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kraj'}), required=False)

	class Meta:
		model = Profil
		fields = ('telefon', 'adres1', 'adres2', 'miasto', 'wojewodztwo', 'kod_pocztowy', 'kraj')


class ChangePassForm(SetPasswordForm):
	class Meta:
		model = User
		fields = ['new_password1', 'new_password2']

	def __init__(self, *args, **kwargs):
		super(ChangePassForm, self).__init__(*args, **kwargs)

		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['placeholder'] = 'Hasło'
		self.fields['new_password1'].label = ''
		self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Hasło nie może być podobne do nazwy użytkownika.</li><li>Twoje hasło musi zawierać conajmniej 8 znaków.</li><li>Hasło nie może być powszechnie używane.</li><li>Nie może się składać wyłącznie z jednego typu znaków.</li></ul>'

		self.fields['new_password2'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['placeholder'] = 'Podaj ponownie hasło'
		self.fields['new_password2'].label = ''
		self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Podaj hasło jeszcze raz dla weryfikacji.</small></span>'



class UpdateForm(UserChangeForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres email'}), required=False)
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię'}), required=False)
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwisko'}), required=False)
	password = None

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email')

	def __init__(self, *args, **kwargs):
		super(UpdateForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Pole wymagane.</small></span>'


class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Adres email'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Imię'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nazwisko'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nazwa użytkownika'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Pole wymagane.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Hasło'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Hasło nie może być podobne do nazwy użytkownika.</li><li>Twoje hasło musi zawierać conajmniej 8 znaków.</li><li>Hasło nie może być powszechnie używane.</li><li>Nie może się składać wyłącznie z jednego typu znaków.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Podaj ponownie hasło'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Podaj hasło jeszcze raz dla weryfikacji.</small></span>'