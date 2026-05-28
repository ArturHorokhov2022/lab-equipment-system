# lab-equipment-system

# System Ewidencji Wyposażenia Laboratorium

## 1. Skład zespołu
Artur Horokhov – Rola: Główny programista, architekt bazy danych, administrator środowiska.
/// – Rola: Analityk wymagań, tester systemu, dokumentalista.

## 2. Opis projektu
Projekt obejmuje realizację webowej aplikacji usprawniającej zarządzanie, ewidencję oraz kontrolę stanu technicznego sprzętu laboratoryjnego na uczelni. System pozwala na kategoryzację zasobów (np. komputery, przyrządy pomiarowe, komponenty sieciowe), przypisywanie im unikalnych numerów inwentarzowych oraz dynamiczną zmianę statusu eksploatacji (Dostępne, W naprawie, Spisane). 

Aplikacja została oparta na architekturze MVC (Model-View-Controller) i zaimplementowana w języku Python z wykorzystaniem frameworka Django oraz wbudowanej bazy danych SQLite.

## 3. Co zostało do tej pory zrealizowane
W ramach dotychczasowych etapów prac (odpowiednik zrealizowanych kamieni milowych w harmonogramie) wykonano:
* Zainicjalizowano repozytorium Git oraz skonfigurowano odizolowane środowisko wirtualne (venv).
* Zaprojektowano i zaimplementowano strukturę relacyjnej bazy danych (modele `Category` oraz `Equipment`).
* Skonfigurowano system mapowania obiektowo-relacyjnego (ORM) oraz pomyślnie przeprowadzono migrację bazy danych.
* Uruchomiono i w pełni spersonalizowano panel administracyjny Django: wdrożono moduł wyszukiwania sprzętu po numerze inwentarzowym oraz panel filtrów bocznych (filtrowanie według kategorii i statusu urządzenia).
* Utworzono konto administratora bezpieczeństwa systemu i przetestowano autoryzację dostępu.

## 4. Mój udział w projekcie (Artur Horokhov)
Jako główny wykonawca komponentów technicznych byłem odpowiedzialny za:
* Przygotowanie architektury bazy danych oraz kodu źródłowego modeli w Pythonie.
* Konfigurację logiki biznesowej panelu administracyjnego (wyszukiwanie, mechanizmy filtrowania).
* Zarządzanie środowiskiem uruchomieniowym oraz rozwiązanie problemów technicznych związanych z konfiguracją powłoki terminala.
* Integrację bazy danych SQLite z panelem zarządzania.

*(Udział drugiego członka zespołu obejmował: analizę wymagań funkcjonalnych, przygotowanie scenariuszy testowych dla operacji CRUD, testowanie walidacji unikalności numerów inwentarzowych oraz współtworzenie dokumentacji technicznej).*
