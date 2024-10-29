"""
Moduł `zadania` zawiera definicje klas dla różnych typów zadań: 
Zadanie, ZadaniePriorytetowe i ZadanieRegularne.

Każda klasa reprezentuje różne aspekty zadania.
"""
class Zadanie:
    """
    Klasa reprezentująca podstawowe zadanie.

    Atrybuty:
    ----------
    tytul : str
        Tytuł zadania.
    opis : str
        Opis zadania.
    termin_wykonania : str
        Termin wykonania zadania.
    czy_wykonane : bool
        Status wykonania zadania.
    szczegoly : str
        Dodatkowe szczegóły zadania.
    informacje : str
        Dodatkowe informacje o zadaniu.
    """
    def __init__(self, tytul, opis, termin_wykonania, czy_wykonane=False, **kwargs):
        """
        Inicjalizuje nowe zadanie.

        Parametry:
        ----------
        tytul : str
            Tytuł zadania.
        opis : str
            Opis zadania.
        termin_wykonania : str
            Termin wykonania zadania.
        czy_wykonane : bool, opcjonalnie
            Status wykonania (domyślnie False).
        **kwargs : dict
            Opcjonalne szczegóły i informacje o zadaniu.
        """
        self.tytul = tytul
        self.opis = opis
        self.termin_wykonania = termin_wykonania
        self.czy_wykonane = czy_wykonane
        self.szczegoly = kwargs.get('szczegoly', '')
        self.informacje = kwargs.get('informacje', '')

    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania.
        
        Zwraca:
        -------
        str
            Sformatowany tekst zawierający szczegóły zadania.
        """
        szczegoly_str = f"\n Szczegóły: {self.szczegoly}" if self.szczegoly else ""
        informacje_str = f"\n Informacje: {self.informacje}" if self.informacje else ""
        return f"______________________________ \n Zadanie: \n Tytuł: {self.tytul}\n Opis: {self.opis}\n Termin: {self.termin_wykonania}\n Wykonane: {self.czy_wykonane}{szczegoly_str}{informacje_str} \n ______________________________"

    def for_file(self):
        """
        Generuje tekst reprezentujący zadanie w formacie do zapisu w pliku.
        
        Zwraca:
        -------
        str
            Tekst reprezentujący zadanie w formacie CSV.
        """
        return f"{self.tytul};{self.opis};{self.termin_wykonania};{self.czy_wykonane};{self.szczegoly};{self.informacje}"

class ZadaniePriorytetowe(Zadanie):
    """
    Klasa reprezentująca zadanie o wysokim priorytecie.

    Atrybuty:
    ----------
    priorytet : str
        Poziom priorytetu zadania.
    """
    def __init__(self, tytul, opis, termin_wykonania, priorytet, czy_wykonane=False, **kwargs):
        """
        Inicjalizuje nowe zadanie priorytetowe.

        Parametry:
        ----------
        tytul : str
            Tytuł zadania.
        opis : str
            Opis zadania.
        termin_wykonania : str
            Termin wykonania zadania.
        priorytet : str
            Poziom priorytetu zadania.
        czy_wykonane : bool, opcjonalnie
            Status wykonania (domyślnie False).
        **kwargs : dict
            Opcjonalne szczegóły i informacje o zadaniu.
        """
        super().__init__(tytul, opis, termin_wykonania, czy_wykonane, **kwargs)
        self.priorytet = priorytet

    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania priorytetowego.
        
        Zwraca:
        -------
        str
            Sformatowany tekst zawierający szczegóły zadania priorytetowego.
        """
        szczegoly_str = f"\n Szczegóły: {self.szczegoly}" if self.szczegoly else ""
        informacje_str = f"\n Informacje: {self.informacje}" if self.informacje else ""
        return f"______________________________ \n Zadanie Priorytetowe:\n Tytuł: {self.tytul} \n Opis: {self.opis}\n Termin: {self.termin_wykonania}\n Priorytet: {self.priorytet}\n Wykonane: {self.czy_wykonane}{szczegoly_str}{informacje_str} \n ______________________________"

    def for_file(self):
        """
        Generuje tekst reprezentujący zadanie priorytetowe w formacie do zapisu w pliku.
        
        Zwraca:
        -------
        str
            Tekst reprezentujący zadanie priorytetowe w formacie CSV.
        """
        return f"P;{self.tytul};{self.opis};{self.termin_wykonania};{self.priorytet};{self.czy_wykonane};{self.szczegoly};{self.informacje}"

class ZadanieRegularne(Zadanie):
    """
    Klasa reprezentująca zadanie regularne.

    Atrybuty:
    ----------
    powtarzalnosc : str
        Częstotliwość powtarzania zadania.
    """
    def __init__(self, tytul, opis, termin_wykonania, powtarzalnosc, czy_wykonane=False, **kwargs):
        """
        Inicjalizuje nowe zadanie regularne.

        Parametry:
        ----------
        tytul : str
            Tytuł zadania.
        opis : str
            Opis zadania.
        termin_wykonania : str
            Termin wykonania zadania.
        powtarzalnosc : str
            Częstotliwość powtarzania zadania.
        czy_wykonane : bool, opcjonalnie
            Status wykonania (domyślnie False).
        **kwargs : dict
            Opcjonalne szczegóły i informacje o zadaniu.
        """
        super().__init__(tytul, opis, termin_wykonania, czy_wykonane, **kwargs)
        self.powtarzalnosc = powtarzalnosc

    def __str__(self):
        """
        Zwraca reprezentację tekstową zadania regularnego.
        
        Zwraca:
        -------
        str
            Sformatowany tekst zawierający szczegóły zadania regularnego.
        """
        szczegoly_str = f"\n Szczegóły: {self.szczegoly}" if self.szczegoly else ""
        informacje_str = f"\n Informacje: {self.informacje}" if self.informacje else ""
        return f"______________________________ \n Zadanie Regularne: \n Tytuł: {self.tytul}\n Opis: {self.opis}\n Termin: {self.termin_wykonania}\n Powtarzalność: {self.powtarzalnosc}\n Wykonane: {self.czy_wykonane}{szczegoly_str}{informacje_str} \n ______________________________"

    def for_file(self):
        """
        Generuje tekst reprezentujący zadanie regularne w formacie do zapisu w pliku.
        
        Zwraca:
        -------
        str
            Tekst reprezentujący zadanie regularne w formacie CSV.
        """
        return f"R;{self.tytul};{self.opis};{self.termin_wykonania};{self.powtarzalnosc};{self.czy_wykonane};{self.szczegoly};{self.informacje}"