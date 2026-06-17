# Instrukcja kompilacji i instalacji

## Wymagania systemowe

- System operacyjny: Windows 10/11, macOS 10.15+, Linux (Ubuntu 20.04+)
- Python 3.10 lub nowszy
- pip (menedżer pakietów Python, instalowany razem z Pythonem)
- Połączenie z Internetem (do pobrania zależności)

## Wymagane biblioteki

| Biblioteka | Wersja | Opis |
|------------|--------|------|
| Django | 4.x lub nowszy | Framework webowy |
| Pillow | 9.0+ | Obsługa plików graficznych (zdjęcia produktów) |

Biblioteki frontendowe ładowane są przez CDN i nie wymagają instalacji:
- Bootstrap 5.2.3
- Bootstrap Icons 1.5.0
- jQuery 4.0.0

## Instalacja krok po kroku

### 1. Rozpakowanie archiwum

Rozpakuj plik `ecom.zip` do wybranego katalogu, np.:

```
C:\projekty\ecom\        (Windows)
/home/uzytkownik/ecom/   (Linux/macOS)
```

### 2. Instalacja Pythona

Pobierz i zainstaluj Python 3.10 lub nowszy ze strony:
https://www.python.org/downloads/

Podczas instalacji na systemie Windows zaznacz opcję **"Add Python to PATH"**.

Sprawdź poprawność instalacji:
```bash
python --version
```

### 3. Tworzenie wirtualnego środowiska (zalecane)

```bash
# Przejdź do katalogu projektu
cd ecom/ecom

# Utwórz wirtualne środowisko
python -m venv venv

# Aktywuj środowisko
# Windows:
venv\Scripts\activate
# Linux/macOS:
source venv/bin/activate
```

### 4. Instalacja zależności

```bash
pip install django pillow
```

### 5. Inicjalizacja bazy danych

```bash
python manage.py migrate
```

### 6. Tworzenie konta administratora

```bash
python manage.py createsuperuser
```

Podaj nazwę użytkownika, adres e-mail i hasło.

### 7. Uruchomienie serwera deweloperskiego

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: **http://127.0.0.1:8000**

Panel administratora dostępny pod adresem: **http://127.0.0.1:8000/admin**

## Struktura katalogów projektu

```
ecom/
└── ecom/
    ├── manage.py          # Skrypt zarządzania Django
    ├── ecom/              # Główna konfiguracja projektu
    │   ├── settings.py    # Ustawienia aplikacji
    │   ├── urls.py        # Główny routing URL
    │   └── wsgi.py        # Konfiguracja WSGI
    ├── sklep/             # Moduł sklepu i kont użytkowników
    ├── koszyk/            # Moduł koszyka zakupowego
    └── payment/           # Moduł zamówień i płatności
```
