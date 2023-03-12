'''   Wojciech Barczynski 410754
    Opis algorytmu:
    Dla k większych od 1:
    Tworzymy K+1 elementowy kopiec minimalny w formie tablicy wskaznikow na kolejne elementy linked listy
    i wybieramy element minimalny (pierwszy). Przychodzac po linked liscie kolejno umieszczamy pojedynczy
    element na pierwsza pozycje kopca i przyrwacamy strukture kopca wywolłujac funkcje heapify(). Po wykonaniu
    funkcji na gorze kopca (na 0 indeksie tablicy rezprezentujacej kopiec) znajduje sie element minimalny, ktory
    dolaczamy do poczatku posortowanej liczy i na jego miejsce wstawiamy kolejny element linked listy i powtarzamy
    operacje. Po dojsciu do konca listy oprozniamy kopiec w sposob analogiczny do dzialania algorytmu heasort.
    Dla k == 1:
    Wykonujemy traverse_sort, ktory przechodzi pop liscie i zamienia elementy, gdy nastepny ma wieksza wartosc od
    poprzedniego.

    N - dlugosc linked listy
    Analiza zlozonosci obliczeniowej:
    DLa k > 1:
    Budowa kopca K+1 elementowego zajmuje O(k+1). przejscie po tablicy to O(N), a wykonanie heapify() to O(log(k)),
    wiec zlozonosc to O(K) + O(N * log(K)) = O(N * log(K))
    Dla k == 1:
    Przjejscie linked listy to O(N).

    Analiza zlozonosci pamieciowej:
    DLa k > 1:
    Poniewaz tworzymy kopiec K+1 elementowy, wiec zlozonosc pamieciowa to O(K).
    DLa k == 1:
    Nie tworzymu zadnej dodoatkowej struktury, wiec zlozonosc to O(1).
'''


from zad1testy import Node, runtests


def traverse_sort(p):  # for k = 1
    if p.next is None:
        return p
    if p.next.val < p.val:
        head = p.next
        p.next.next, p.next = p, p.next.next
        p = head.next
    else:
        head = p
        p = p.next

    prev = head
    while p.next is not None:
        if p.next.val < p.val:
            prev.next, p.next.next, p.next = p.next, p, p.next.next
            prev = prev.next
        else:
            prev = p
            p = p.next

    return head


def heapify(T, n, i):
    l = 2 * i + 1
    r = 2 * i + 2
    min = i
    if l < n and T[l].val < T[min].val:
        min = l
    if r < n and T[r].val < T[min].val:
        min = r
    if min != i:
        T[i], T[min] = T[min], T[i]
        heapify(T, n, min)


def build_heap(T):
    n = len(T)
    for i in range((n - 1) // 2, -1, -1):
        heapify(T, n, i)


def SortH(p, k):
    if k == 0:
        return p
    if k == 1:
        return traverse_sort(p)

    pointer_array = []
    steps_left = k
    while steps_left >= 0 and p is not None:
        pointer_array.append(p)
        p = p.next
        steps_left -= 1
    n = len(pointer_array)
    build_heap(pointer_array)

    head = pointer_array[0]
    tmp = pointer_array[0]

    while p is not None:
        pointer_array[0] = p
        heapify(pointer_array, n, 0)
        tmp.next = pointer_array[0]
        tmp = pointer_array[0]
        p = p.next

    pointer_array[0] = pointer_array[len(pointer_array) - 1]
    for i in range(len(pointer_array) - 1, 0, -1):
        heapify(pointer_array, i, 0)
        tmp.next = pointer_array[0]
        tmp = pointer_array[0]
        pointer_array[0] = pointer_array[i - 1]

    tmp.next = None
    return (head)


runtests(SortH)
