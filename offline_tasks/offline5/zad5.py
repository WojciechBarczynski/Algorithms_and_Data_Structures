# Wojciech Barczynski 410754
'''
Opis algorytmu:
Zauwazmy, ze aby dotrzec do konca trasy, nalezy zebrac co najmniej n - 1 paliwa.
Paliwo mozemy wybierac z dostepnych stacji, czyli tych, do ktorych mozemy dojechc.
Zwrocmy uwage, iz kolejnosc w jakiej nasz algorytm wybiera stacje nie ma znaczenia
(np. stacja o indeksie 3 jest przed staja o indeksie 1), gdyz ustalajac trase, mozemy posortowac
wybrana trase, wedlug kolejnosci stacji. Aby wybrac najbardziej optymalna trase, tworzymy kolejke
priorytetowa dostepych stacji (kopiec maksymalny), z ktorego wybieramy najbardziej oplacalny element
(element o najwyzszej wartosci), a nastepnie dodajemy do kolejki stacje, do ktorych
uzyskalismy dostep dzieki wybraniu naszej stacji). Nastepnie sortujemy wybrane stacje wedlug indeksow.

Dowod poprawnosci (nie jest formalny, bo i tak nikt tego nie czyta):
W kazdym momencie bierzemy najbardziej oplacalny element, a dzieki zastosowaniu kolejki priorytetowej nie wykluczmay
wyboru zadnego z dostepnych elementow. Jezeli wybralibysmy inny element, to nie moglibysmy osiagnac celowej sumy
paliwa w mniejszej liczbie wybranych stacji, gdyz zamieniajac w wyborze ten element z optymalny, uzyskujemy wieksza sume.
'''


from zad5testy import runtests
from queue import PriorityQueue


def plan(T):
    n = len(T)
    selected_stations_list = [0]
    accessible_stations = PriorityQueue()
    last_possible_index = T[0]

    # dodajemy do kolejki stacje, o ktorych mamy dostep
    for i in range(1, last_possible_index + 1):
        accessible_stations.put((T[i] * (-1), i))

    while last_possible_index < n - 1:  # dopoki nie mozemy dojechac do konca
        maximal_value_in_pq, max_val_in_pq_list_index = accessible_stations.get()
        selected_stations_list += [max_val_in_pq_list_index]
        maximal_value_in_pq *= -1
        for i in range(last_possible_index + 1, min(last_possible_index + maximal_value_in_pq + 1, n)):  # dodajemy
            # stacje, do ktorych uzyskalismy dostep
            accessible_stations.put((T[i] * (-1), i))
        last_possible_index += maximal_value_in_pq  # przesowamy dostepny horyzont

    selected_stations_list.sort()  # sortujemy indeksy

    return selected_stations_list


runtests(plan, all_tests=True)
