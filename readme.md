# Menager Zadań
W tym programie możesz dodawać zadania do wykonania
## Instalacja
1. Sklonuj repo: `git clone https://github.com/TomaszSzlotawa/TaskManager.git`
2. Wejdź do katalogu projektu: `cd TaskManager`
3. Zainstaluj zależności: `pip install -r reqiurements.txt`
## Użycie
- Uruchom program.py

``` python
def decrator(func):
    def wrapper():
        os.system('cls' if os.name == 'nt' else 'clear')
        start_time = datetime.datetime.now()
        func()
        end_time = datetime.datetime.now()
        print(f"Czas wykonania: {end_time - start_time}")
    return wrapper
```

## Dokumentacja
Dokumentacja znajduje się w pliku program_documentation.html

## Autor
Tomasz Szlotawa

## Licencja
MIT License
