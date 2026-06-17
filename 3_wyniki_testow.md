# Wyniki scenariuszy testowych

## Informacje ogólne

Testowanie aplikacji przeprowadzono manualnie przez analizę scenariuszy testowych zdefiniowanych w rozdziale szóstym pracy. Środowisko testowe: Python 3.13, Django, SQLite, system Windows 11. Wszystkie testy przeprowadzono na lokalnym serwerze deweloperskim.

---

## Scenariusz 1: Rejestracja nowego użytkownika

**Dane wejściowe:**
- Nazwa użytkownika: `testuser`
- Imię: Jan
- Nazwisko: Kowalski
- E-mail: jan.kowalski@test.pl
- Hasło: TestHaslo123!

**Kroki:**
1. Przejście na stronę rejestracji.
2. Wypełnienie formularza i zatwierdzenie.

**Oczekiwany wynik:**
- Utworzenie rekordu `User` w bazie danych.
- Automatyczne utworzenie rekordów `Profil` i `AdresWysylki`.
- Automatyczne zalogowanie użytkownika.
- Przekierowanie do formularza uzupełnienia danych adresowych.

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

**Uwagi:** Sygnały `post_save` poprawnie wyzwoliły się i utworzyły powiązane rekordy w bazie.

---

## Scenariusz 2: Logowanie z odtworzeniem koszyka

**Dane wejściowe:**
- Nazwa użytkownika: `testuser`
- Hasło: TestHaslo123!
- Stan koszyka w `koszyk_old`: produkt ID 1, ilość 2

**Kroki:**
1. Wylogowanie z konta.
2. Dodanie produktu do koszyka jako gość.
3. Zalogowanie na konto testowe.

**Oczekiwany wynik:**
- Zainicjowanie sesji uwierzytelnionej.
- Odtworzenie stanu koszyka z pola `koszyk_old`.
- Koszyk zawiera produkty z poprzedniej sesji.

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

---

## Scenariusz 3: Złożenie zamówienia przez gościa

**Dane wejściowe:**
- Produkt: naszyjnik srebrny, ilość 1
- Dane wysyłki: Anna Nowak, ul. Testowa 1, Warszawa, 00-001, Polska
- Dane rozliczeniowe: wypełnione

**Kroki:**
1. Dodanie produktu do koszyka jako gość.
2. Przejście do kasy i wypełnienie formularza danych wysyłki.
3. Zatwierdzenie danych rozliczeniowych.
4. Finalizacja zamówienia.

**Oczekiwany wynik:**
- Rekord `Zamowienia` z pustym polem `uzytkownik`.
- Rekordy `ZamowieniaProdukty` z poprawną ilością i zamrożoną ceną.
- Koszyk sesji wyczyszczony.

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

**Uwagi:** Pole `uzytkownik` ma wartość NULL co potwierdza poprawną obsługę zamówień gości.

---

## Scenariusz 4: Zmiana statusu zamówienia przez administratora

**Dane wejściowe:**
- Zamówienie nr 1, status: `wyslane=False`

**Kroki:**
1. Zalogowanie jako superużytkownik.
2. Przejście do panelu zamówień oczekujących.
3. Kliknięcie przycisku wysyłki dla zamówienia nr 1.

**Oczekiwany wynik:**
- Rekord `Zamowienia` ze statusem `wyslane=True`.
- Pole `data_wyslania` uzupełnione bieżącą datą i godziną.

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

**Uwagi:** Sygnał `pre_save` poprawnie wykrył zmianę statusu i automatycznie uzupełnił pole `data_wyslania`. Widok nie wykonuje żadnych operacji na polu daty.

---

## Scenariusz 5: Ochrona panelu administratora

**Dane wejściowe:**
- Użytkownik: `testuser` (bez uprawnień superużytkownika)

**Kroki:**
1. Zalogowanie jako zwykły użytkownik.
2. Próba ręcznego wpisania adresu URL panelu zamówień.

**Oczekiwany wynik:**
- Brak dostępu do panelu.
- Przekierowanie na stronę główną.
- Komunikat „Odmowa dostępu".

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

---

## Scenariusz 6: Wyszukiwanie produktu

**Dane wejściowe:**
- Fraza wyszukiwania: „naszyjnik"

**Kroki:**
1. Wpisanie frazy w pole wyszukiwania.
2. Zatwierdzenie wyszukiwania.

**Oczekiwany wynik:**
- Lista produktów których nazwa lub opis zawiera frazę „naszyjnik".

**Wynik uzyskany:** ✅ Zgodny z oczekiwanym.

---

## Podsumowanie wyników

| Scenariusz | Wynik |
|------------|-------|
| Rejestracja nowego użytkownika | ✅ Zaliczony |
| Logowanie z odtworzeniem koszyka | ✅ Zaliczony |
| Złożenie zamówienia przez gościa | ✅ Zaliczony |
| Zmiana statusu zamówienia przez administratora | ✅ Zaliczony |
| Ochrona panelu administratora | ✅ Zaliczony |
| Wyszukiwanie produktu | ✅ Zaliczony |

Wszystkie zidentyfikowane wymagania funkcjonalne zostały spełnione.
