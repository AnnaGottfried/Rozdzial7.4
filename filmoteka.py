import random


class Film:
    liczba_odtw = 0

    def __init__(self, tytul, rok, gatunek, liczba_odtw):
        self.tytul = tytul
        self.rok = rok
        self.gatunek = gatunek
        self.liczba_odtw = liczba_odtw

    def play(self):
        liczba_odtw += 1
        '''Po wyświetleniu filmu jako string widoczne są tytuł i rok wydania np. “Pulp Fiction (1994)”.'''

    def __str__(self):
        return f" {self.tytul} {self.rok}"


class Serial(Film):

    def __init__(self, numer_odc, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odc = numer_odc
        self.numer_sezonu = numer_sezonu

    #def play(self):
    #    liczba_odtw += 1

    '''Po wyświetleniu serialu jako string, pokazują się informacje o konkretnym odcinku,
     np.: “The Simpsons S01E05”
     (gdzie po S pokazany jest numer sezonu w notacji dwucyfrowej,
      natomiast po E - numer odcinka, również w zapisie dwucyfrowym)    '''

    def __str__(self):
        return f" {self.tytul} {self.numer_sezonu}{self.numer_odc}"


biblioteka = []

biblioteka.append(
    Serial(tytul="The Simpsons", rok="1995", gatunek="serial", liczba_odtw=0, numer_sezonu="S01", numer_odc="E05"))
biblioteka.append(Film(tytul="French Kiss", rok="1998", gatunek="film", liczba_odtw=0))
biblioteka.append(
    Serial(tytul="Hallo Hallo", rok="1985", gatunek="serial", liczba_odtw=0, numer_sezonu="S01", numer_odc="E09"))
biblioteka.append(Film(tytul="Wszystko co słyszą kobiety", rok="2004", gatunek="film", liczba_odtw=0))
biblioteka.append(
    Serial(tytul="Sex and the City", rok="1999", gatunek="serial", liczba_odtw=0, numer_sezonu="S02", numer_odc="E15"))
biblioteka.append(Film(tytul="Brigitte Jones", rok="2000", gatunek="film", liczba_odtw=0))
biblioteka.append(Film(tytul="Rambo", rok="1986", gatunek="film", liczba_odtw=0))
biblioteka.append(Film(tytul="Nietykalni", rok="2011", gatunek="film", liczba_odtw=0))
biblioteka.append(Film(tytul="Lista Schindlera", rok="1995", gatunek="film", liczba_odtw=0))

#lista_filmow = []
# lista_seriali = []


def get_movies():
    lista_filmow = []
    for item in biblioteka:

        # print(biblioteka[item].gatunek)
        if item.gatunek == 'film':
            lista_filmow.append(item.tytul)

    return lista_filmow


def get_series():
    lista_seriali=[]
    for item in biblioteka:

        if item.gatunek == 'serial':
            lista_seriali.append(item.tytul)

    return lista_seriali


wynik = get_movies()
wynik.sort()
print(f"Lista filmów: {wynik} ")

wynik1 = get_series()
wynik1.sort()
print(f"Lista seriali: {wynik1}")
print("*" * 70)


def search(szukany_tytul):
    for item in biblioteka:

        if item.tytul == szukany_tytul:
            print(f'Szukany film to: {item}')


def generate_views():
    dlugosc = len(biblioteka)
    n = random.randint(0, dlugosc - 1)
    losowo = random.randint(0, 100)

    biblioteka[n].liczba_odtw = losowo


#    print(biblioteka[n].liczba_odtw)


def multiple_views():
    for item in range(10):
        generate_views()


def sorttitles(movie):
    return movie.liczba_odtw


'''
def top_titles():
    biblioteka.sort(key=lambda x: x.liczba_odtw, reverse=True)
    for obj in biblioteka:
        print("Najlepsze filmy: " +str(obj.tytul) + " z rankingiem: " +str(obj.liczba_odtw))
'''


def top_titles(kategoria):
    biblioteka.sort(key=lambda x: x.liczba_odtw, reverse=True)
    for obj in biblioteka:
        if kategoria == "serial":
            if obj.gatunek == "serial":
                print("Najlepsze seriale: " + str(obj.tytul) + " z rankingiem: " + str(obj.liczba_odtw))
        else:
            if obj.gatunek == "film":
                print("Najlepsze filmy: " + str(obj.tytul) + " z rankingiem: " + str(obj.liczba_odtw))


search("Sex and the City")
multiple_views()
top_titles('film')