# Instrukcja użytkowania aplikacji (Manual)

## Informacje ogólne

Aplikacja webowa do zarządzania sprzedażą osobistą przez Internet umożliwia prowadzenie sklepu internetowego z biżuterią. System obsługuje trzy typy użytkowników: gościa, zarejestrowanego klienta oraz administratora.

Adres aplikacji po uruchomieniu lokalnym: **http://127.0.0.1:8000**

---

## 1. Użytkownik niezalogowany (Gość)

### Przeglądanie produktów

1. Otwórz stronę główną aplikacji.
2. Na stronie głównej wyświetlona jest siatka produktów ze zdjęciami, nazwami i cenami.
3. Produkty objęte promocją wyświetlają przekreśloną cenę regularną i cenę promocyjną.
4. Kliknij na produkt aby przejść do strony ze szczegółami.

### Przeglądanie według kategorii

1. W pasku nawigacyjnym kliknij nazwę kategorii.
2. Zostanie wyświetlona lista produktów należących do wybranej kategorii.

### Wyszukiwanie produktów

1. W pasku nawigacyjnym kliknij ikonę wyszukiwania.
2. Wpisz szukaną frazę w pole wyszukiwania i zatwierdź.
3. Wyświetlone zostaną produkty których nazwa lub opis zawiera szukaną frazę.

### Dodawanie produktu do koszyka

1. Przejdź na stronę szczegółów produktu.
2. Kliknij przycisk **„Dodaj do koszyka"**.
3. Licznik koszyka w pasku nawigacyjnym zaktualizuje się automatycznie.

### Koszyk zakupowy

1. Kliknij ikonę koszyka w pasku nawigacyjnym.
2. Wyświetlona zostanie lista produktów w koszyku wraz z ilościami i cenami.
3. Aby zmienić ilość – wpisz nową wartość w pole ilości i kliknij **„Aktualizuj"**.
4. Aby usunąć produkt – kliknij przycisk **„Usuń"** przy danej pozycji.
5. Na dole widoku wyświetlana jest łączna wartość koszyka.

### Składanie zamówienia

1. W widoku koszyka kliknij przycisk **„Zamów"**.
2. Wypełnij formularz danych wysyłki (imię i nazwisko, adres, miasto, kraj, kod pocztowy).
3. Kliknij **„Kontynuuj"**.
4. Sprawdź dane rozliczeniowe i kliknij **„Złóż zamówienie"**.
5. Zamówienie zostanie zarejestrowane w systemie, a koszyk wyczyszczony.

### Rejestracja konta

1. Kliknij **„Zarejestruj się"** w pasku nawigacyjnym.
2. Wypełnij formularz: nazwa użytkownika, imię, nazwisko, adres e-mail, hasło.
3. Po pomyślnej rejestracji zostaniesz automatycznie zalogowany.
4. Uzupełnij dane adresowe w formularzu który się pojawi.

---

## 2. Zarejestrowany klient

### Logowanie

1. Kliknij **„Zaloguj się"** w pasku nawigacyjnym.
2. Podaj nazwę użytkownika i hasło.
3. Kliknij **„Zaloguj"**.
4. Koszyk z poprzedniej sesji zostanie automatycznie odtworzony.

### Edycja danych osobowych

1. Po zalogowaniu kliknij menu użytkownika w pasku nawigacyjnym.
2. Wybierz **„Edytuj dane"**.
3. Zmień imię, nazwisko lub adres e-mail i kliknij **„Zapisz"**.

### Aktualizacja adresu wysyłki

1. Z menu użytkownika wybierz **„Adres wysyłki"**.
2. Zaktualizuj dane adresowe i kliknij **„Zapisz"**.
3. Przy następnym zamówieniu formularz zostanie wstępnie wypełniony tymi danymi.

### Zmiana hasła

1. Z menu użytkownika wybierz **„Zmień hasło"**.
2. Podaj nowe hasło i jego potwierdzenie.
3. Kliknij **„Zmień hasło"**.

### Wylogowanie

1. Kliknij menu użytkownika w pasku nawigacyjnym.
2. Wybierz **„Wyloguj się"**.

---

## 3. Administrator

Administrator loguje się tak samo jak zwykły klient. Po zalogowaniu w pasku nawigacyjnym pojawia się dodatkowe menu **„Panel administratora"**.

### Panel zamówień oczekujących

1. Kliknij **„Panel administratora"** → **„Zamówienia oczekujące"**.
2. Wyświetlona zostanie lista zamówień ze statusem „niewysłane".
3. Dla każdego zamówienia widoczne są: numer, imię i nazwisko klienta, kwota, data złożenia.
4. Kliknij numer zamówienia aby zobaczyć szczegóły (pozycje, adresy).
5. Aby oznaczyć zamówienie jako wysłane – kliknij przycisk **„Wyślij"** przy danym zamówieniu.
6. System automatycznie zapisze datę i godzinę wysyłki.

### Panel zamówień wysłanych

1. Kliknij **„Panel administratora"** → **„Zamówienia wysłane"**.
2. Wyświetlona zostanie lista zamówień ze statusem „wysłane" wraz z datą ekspedycji.
3. Aby cofnąć status wysyłki – kliknij przycisk **„Cofnij wysyłkę"**.

### Zarządzanie produktami i kategoriami

Produkty i kategorie zarządzane są przez wbudowany panel administracyjny Django:

1. Przejdź pod adres: **http://127.0.0.1:8000/admin**
2. Zaloguj się danymi superużytkownika.
3. W sekcji **„Sklep"** wybierz **„Produkty"** lub **„Kategorie"**.
4. Kliknij **„Dodaj produkt"** aby dodać nowy produkt.
5. Wypełnij pola: nazwa, cena, opis, kategoria, zdjęcie.
6. Jeśli produkt jest objęty promocją – zaznacz pole **„Czy promocja"** i podaj cenę promocyjną.
7. Kliknij **„Zapisz"**.
