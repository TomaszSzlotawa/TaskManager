from zadania import ZadaniePriorytetowe, ZadanieRegularne



class ManagerZadan:
    """
    Klasa ManagerZadan zarządza listą zadań, umożliwiając dodawanie, usuwanie, edytowanie oraz oznaczanie zadań jako wykonane.
    Metody:
    --------
    __init__():
        Inicjalizuje pustą listę zadań.
    dodaj_zadanie(zadanie):
        Dodaje zadanie do listy zadań.
    usun_zadanie(tytul: str):
        Usuwa zadanie o podanym tytule z listy zadań.
    oznacz_jako_wykonane(tytul: str):
        Oznacza zadanie o podanym tytule jako wykonane.
    edytuj_zadanie(tytul: str, nowy_tytul=None, nowy_opis=None, nowy_termin=None, nowy_priorytet=None, nowa_powtarzalnosc=None):
        Edytuje zadanie o podanym tytule, zmieniając jego tytuł, opis, termin wykonania, priorytet lub powtarzalność.
    __contains__(tytul: str):
        Sprawdza, czy zadanie o podanym tytule znajduje się na liście zadań.
    """
    def __init__(self):
        self.zadania = []
    1

    def dodaj_zadanie(self, zadanie):
        self.zadania.append(zadanie)
    
    def usun_zadanie(self, tytul=str):
        self.zadania = [zadanie for zadanie in self.zadania if zadanie.tytul != tytul]
    
    def oznacz_jako_wykonane(self, tytul=str):
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                zadanie.czy_wykonane = True
    
    def edytuj_zadanie(self, tytul=str, nowy_tytul=None, nowy_opis=None, nowy_termin=None, nowy_priorytet=None, nowa_powtarzalnosc=None):
        for zadanie in self.zadania:
            if zadanie.tytul == tytul:
                if nowy_tytul:
                    zadanie.tytul = nowy_tytul
                if nowy_opis:
                    zadanie.opis = nowy_opis
                if nowy_termin:
                    zadanie.termin_wykonania = nowy_termin
                if isinstance(zadanie, ZadaniePriorytetowe) and nowy_priorytet:
                    zadanie.priorytet = nowy_priorytet
                if isinstance(zadanie, ZadanieRegularne) and nowa_powtarzalnosc:
                    zadanie.powtarzalnosc = nowa_powtarzalnosc
    
    def __contains__(self, tytul=str):
        return any(zadanie.tytul == tytul for zadanie in self.zadania)
