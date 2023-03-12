'''     Wojciech Barczynski 410754
Opis algorytmu: Tworzymy kopie listy L jako liste sorted_by_end_list[]. Nastepnie sortujemy funkcja
quick_sort_by_begging() rosnaco liste L po pierwszej wspolrzednej (poczatku przedzialu),
a w przypadku gdy poczatki przedzialu sa takie same, to sortujemy malejaco po koncu przedzialu
(jezeli mamy dwa przedzialy [a, b] oraz [a, c] i b > c to po posortowaniu wczesniej bedzie przedzial [a, b], ponadto
przedzial [a,c] bedzie sie z nim zawieral). Nastepnie sortujemy liste sorted_by_end_list[] po koncach przedzialu,
używajac funkcji quick_sort_by_ending(). Przechodzac po posortowanej liscie L dla kazdego przedzialu odczytujemy jego
koniec i szukamy binarnie pozycji pierwszego przedzialu o silnie wiekszym koncu przedialu od naszego obecnego przedzialu
z listy L używajac funkcji binary_search() i obliczamy wspolczynnik current_depth jako:
n - 1 - i gdy sorted_by_end_list[n-1][1] == L[i][1]
n - 1 - i - (n - binary_search(sorted_by_end_list, L[i][1], 0, n-1))
gdzie: n - liczba wszystkich przedzialow,  1 - odejmujemy obecny przedzial, i - indeks naszego przedzialu w L,
(n - binary_search(sorted_by_end_list, L[i][1], 0, n-1)) - liczba przedzialow konczacych sie za naszym przedzialem,
i jest rowniez liczba przedzialow rozpoczynajacych sie przed i-tym przedzialem (lub przedzialow o takim samym poczatku,
ale wiekszym lub rownym koncu).
Jezeli wspolczynnik jest wiekszy od max_depth, to aktualizujemy max_depth. Petle przechodzaca po L konczymy, gdy
elementow pozostalych do konca listy jest mniej niz max_depth lub gdy docieramy do konca list (gdy max_depth == 0).

Uzasadnienie poprawnosci algorytmu:
Lemat 1: Przedzial p o max depth nie jest zawarty w zadnym z przedzialow.
    Dowod nie w prost: Jesli istnieje przedzial k, ktory zawiera p, to zawiera on wyszstkie przedzialy,
    ktore zawiera p, wiec zawiera on przynajmniej max depth + 1 przedzialow, co jest sprzeczne z zalozeniem,
    ze p ma max depth, wiec k nie moze istniec, co dowodzi teze.

Zauwazmy, ze depth przedzialu p mozemy opisac wzorem:
depth = liczba wszystkich przedzialow - 1 - liczba przedzialow rozpoczynajacych sie przed p - liczba przedzialow
konczocych sie za p + liczba przedzialow zaczynajacych sie przed i konczacych sie za p.

Zauwazmy, ze ostatnich skladnik w powyzszym rownaniu jest liczba przedzialow, w ktorych zawiera sie przedzial p, wiec
dla przedzialu o max depth jest on rowny 0 na podstawie lematu 1, wiec wspolczynnik current_depth jest rowny
depth przedzialu o maksymalnej glebokosci (jesli jest kilka takich samuch przedzialow, to bedzie on rowny max depth
dla pierwszego w L po posortowaniu), a dla pozostalych przedzialow jest on <= ich depth (gdyz ostatni skladnik
powyzszej sumy jest 0 lub liczba naturalna), wiec masz algorytm z pewnoscia poprawnie obliczy depth przedzialu
o max_depth, a pozostale przedzialy beda mialy mniejszy wspolczynnik, gdyz ich depth jest mniejszy.

Złożoność obliczeniowa:
2 razy sortujemy liste o dlugosci n (2*nlogn), a nastepnie liniowo przechodzimy przez liste o dlugosci n i szukamy
biarnie w drugiej liscie o dlugosci n (logn), wiec mamy: 2*O(nlogn) + O(nlogn) = O(nlogn). Teoretycznie funkcja
sortujaca quicksort moze dzialac w czasie O(n^2), lecz jest to niezwykle rzadki przypadek, wiec nie oplaca sie jej
zamieniac na funkcje heapsort lub mergesort.

Złożoność pamięciowa:
Tworzymy dodatkowa liste dlugosci n O(n) i wykonujemy quicksorta (O(n)), wiec O(n) + O(n) = O(n)
'''

from zad2testy import runtests


def partition_by_begging(L, p, r):
    x = L[r]
    i = p - 1
    for j in range(p, r):
        if L[j][0] < x[0] or (L[j][0] == x[0] and L[j][1] > x[1]):
            i += 1
            L[i], L[j] = L[j], L[i]
    L[i+1], L[r] = L[r], L[i+1]
    return i + 1


def quick_sort_by_begging(L, p, r):
    if p < r:
        q = partition_by_begging(L, p, r)
        quick_sort_by_begging(L, p, q-1)
        quick_sort_by_begging(L, q+1, r)


def partition_by_ending(sorted_by_end_list, p, r):
    x = sorted_by_end_list[r]
    i = p - 1
    for j in range(p, r):
        if sorted_by_end_list[j][1] < x[1]:
            i += 1
            sorted_by_end_list[i], sorted_by_end_list[j] = sorted_by_end_list[j], sorted_by_end_list[i]
    sorted_by_end_list[i+1], sorted_by_end_list[r] = sorted_by_end_list[r], sorted_by_end_list[i+1]
    return i + 1


def quick_sort_by_ending(sorted_by_end_list, p, r):
    if p < r:
        q = partition_by_ending(sorted_by_end_list, p, r)
        quick_sort_by_ending(sorted_by_end_list, p, q-1)
        quick_sort_by_ending(sorted_by_end_list, q+1, r)


def binary_search(T, n, begging, ending):
    if begging == ending:
        return begging
    mid = (begging + ending) // 2
    if T[mid][1] <= n:
        return binary_search(T, n, mid + 1, ending)
    else:
        return binary_search(T, n, begging, mid)


def depth(L):
    n = len(L)
    sorted_by_end_list = [L[i] for i in range(n)]
    quick_sort_by_begging(L, 0, n-1)
    quick_sort_by_ending(sorted_by_end_list, 0, n-1)

    max_depth = 0
    for i in range(n):
        if n - i - 1 < max_depth:
            break
        end = L[i][1]
        if sorted_by_end_list[n-1][1] == end:
            current_depth = n - 1 - i
        else:
            current_depth = n - 1 - i - (n - binary_search(sorted_by_end_list, end, 0, n-1))
        if current_depth > max_depth:
            max_depth = current_depth
    return max_depth


runtests(depth)