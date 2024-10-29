import datetime
from zadania import Zadanie, ZadaniePriorytetowe, ZadanieRegularne
from manager import ManagerZadan
import os
import pydoc


modules = ["zadania", "program", "manager"]

for module_name in modules:
    with open(f"{module_name}_documentation.html", "w") as f:
        f.write(pydoc.HTMLDoc().docmodule(__import__(module_name)))
        print(f"Dokumentacja HTML dla modułu {module_name} została zapisana.")

with open("project_documentation.html", "w") as f:
    for module_name in modules:
        f.write(f"<h1>Documentation for {module_name}</h1>")
        f.write(pydoc.HTMLDoc().docmodule(__import__(module_name)))
    print("Dokumentacja HTML dla całego projektu została zapisana w pliku project_documentation.html.")



def menu():
    print("Menu:")
    print("1. Wyświetl zadania")
    print("2. Dodaj zadanie")
    print("3. Usuń zadanie")
    print("4. Oznacz jako wykonane")
    print("5. Edytuj zadanie")
    print("6. Pokaż najpilniejsze zadania")
    print("7. Zapisz zadania do pliku")
    print("8. Wczytaj zadania z pliku")
    print("9. Wyjście")

manager = ManagerZadan()

def decrator(func):
    def wrapper():
        os.system('cls' if os.name == 'nt' else 'clear')
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"Czas wykonania: {end_time - start_time}")
    return wrapper

@decrator
def opcja_1():
    print("Lista zadań:")
    for zadanie in manager.zadania:
        print(zadanie)
    print()

@decrator
def opcja_2():
    tytul = input("Podaj tytuł zadania: ")
    opis = input("Podaj opis zadania: ")
    termin = input("Podaj termin wykonania zadania(dd.mm.rrrr): ")
    szczegoly = input("Podaj szczegóły zadania: ")
    informacje = input("Podaj dodatkowe informacje o zadaniu: ")
    typ = input("Czy zadanie jest priorytetowe (p) czy regularne (r)? ")
    
    if typ == 'p':
        priorytet = input("Podaj priorytet zadania: ")
        zadanie = ZadaniePriorytetowe(tytul, opis, termin, priorytet, szczegoly=szczegoly, informacje=informacje)
    elif typ == 'r':
        powtarzalnosc = input("Podaj powtarzalność zadania: ")
        zadanie = ZadanieRegularne(tytul, opis, termin, powtarzalnosc, szczegoly=szczegoly, informacje=informacje)
    else:
        zadanie = Zadanie(tytul, opis, termin, szczegoly=szczegoly, informacje=informacje)
    
    manager.dodaj_zadanie(zadanie)
    print("Dodano zadanie.")

@decrator
def opcja_3():
    tytul = input("Podaj tytuł zadania do usunięcia: ")
    manager.usun_zadanie(tytul)
    print("Usunięto zadanie.")

@decrator
def opcja_4():
    tytul = input("Podaj tytuł zadania do oznaczenia jako wykonane: ")
    manager.oznacz_jako_wykonane(tytul)
    print("Oznaczono zadanie jako wykonane.")

@decrator
def opcja_5():
    tytul = input("Podaj tytuł zadania do edycji: ")
    nowy_tytul = input("Podaj nowy tytuł (pozostaw puste, aby nie zmieniać): ")
    nowy_opis = input("Podaj nowy opis (pozostaw puste, aby nie zmieniać): ")
    nowy_termin = input("Podaj nowy termin (pozostaw puste, aby nie zmieniać): ")
    nowy_priorytet = input("Podaj nowy priorytet (pozostaw puste, aby nie zmieniać): ")
    nowa_powtarzalnosc = input("Podaj nową powtarzalność (pozostaw puste, aby nie zmieniać): ")
    manager.edytuj_zadanie(tytul, nowy_tytul, nowy_opis, nowy_termin, nowy_priorytet, nowa_powtarzalnosc)
    print("Edytowano zadanie.")



@decrator
def opcja_6():
    zadania_do_zrobienia = [zadanie for zadanie in manager.zadania if not zadanie.czy_wykonane]
    zadania_do_zrobienia.sort(key=lambda zadanie: datetime.datetime.strptime(zadanie.termin_wykonania, "%d.%m.%Y"))
    print("Zadania do zrobienia (posortowane po terminie):")
    for zadanie in zadania_do_zrobienia:
        print(zadanie)
    print()

@decrator
def opcja_7():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    with open(nazwa_pliku, 'w') as f:
        for zadanie in manager.zadania:
            f.write(zadanie.for_file() + '\n')

@decrator
def opcja_8():
    nazwa_pliku = input("Podaj nazwę pliku: ")
    with open(nazwa_pliku, 'r') as f:
        for line in f:
            zadanie = line.strip().split(';')     
            if len(zadanie) == 6:
                manager.dodaj_zadanie(Zadanie(zadanie[0], zadanie[1], zadanie[2], zadanie[3]))
            elif len(zadanie) == 8:
                if zadanie[0] == 'P':
                    manager.dodaj_zadanie(ZadaniePriorytetowe(zadanie[1], zadanie[2], zadanie[3], zadanie[4], zadanie[5], szczegoly=zadanie[6], informacje=zadanie[7]))
                else:
                    manager.dodaj_zadanie(ZadanieRegularne(zadanie[1], zadanie[2], zadanie[3], zadanie[4], zadanie[5], szczegoly=zadanie[6], informacje=zadanie[7]))


def wyjscie():
    print("Wyjście z programu.")
    return True

def main():
    options = {
        '1': opcja_1,
        '2': opcja_2,
        '3': opcja_3,
        '4': opcja_4,
        '5': opcja_5,
        '6': opcja_6,
        '7': opcja_7,
        '8': opcja_8,
        '9': wyjscie
    }
    
    while True:
        menu()
        choice = input("Wybierz opcję (1-9): ")
        action = options.get(choice)
        if action:
            if action() == True:
                break
        else:
            print("Nieprawidłowy wybór, spróbuj ponownie.")

if __name__ == "__main__":
    main()


