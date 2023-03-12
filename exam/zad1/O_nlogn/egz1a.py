# Wojciech Barczyński 410754
'''
Opis algorytmu: Zauważmy, że jeśli mamy wybrane dane k pól do wzięcia, z których 
każdy ma na tyle śniegu, aby nie stopić się do końca zbierania, to kolejność zbierania
możemy wybrać tak, aby zawsze zebrać śnieg z danego pola przed przejachaniem przez nie,
bez wpływu na ilość zebranego śniegu (zbierzemy śnieg z wszystkich wybranych,
a suma stopionego śniegu na tych polach jest niezależna od koolejności zbirania).

Zauważmy, że gdy mamy wybrane k pól śniegu, to dobranie kolejnoego pola zwiększa ilość
zebranego śniegu tylko wtedy, gdy na tym polu znajduje się więcej śniegu niż k (zabranie
tego śniegu z i-tego pola dodaje S[i] śniegu, ale sprawia, że k śniegu z poprzednio wybranych pól
ulegnie stopnienu przy zbieraniu (używająć optymalnego algorytmu zbieranie opisanego powyżej)).
Oznacza to, że możemy po prostu wybrać taki największy możliwy podzbiór A z S, że len(A) < min(A).
Suma zebranych śniegów wybierając ten pozdbiór będzie największą możliwą na podstawie powyższych
obserwacji.

Złożoność obliczeniowa: O(nlogn) - sort
Złożoność pamięciowa: O(n)
'''

from egz1atesty import runtests


def snow(S):
    return sum([value - index for index, value in enumerate(sorted(S, reverse=True)) if value > index])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)