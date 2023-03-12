# Wojciech Barczyński 410754
'''
Opis algorytmu: Zauważmy, że aby zmaksymalizować ilość zebranego ściegu wystarczy od sum całego ściegu odjąć minimalną
stratę śniegu. Zauważmy, że w każdym dniu opłaca się zebrać przynajmniej jeden śnieg.
Definiujemy więc funkcję minimize_loss(lewa_strona, prawa_strona_dzień, dzień), która opisuje mimimalną stratę śniegu
na przedziale [lewa_strona, prawa_strona] prz założeniu, że przychodzimy tam w dniu dzień. Zauważmy, że
minimize_loss(lewa_strona, prawa_strona_dzień, dzień) = min(minimize_loss(lewa_strona, k - 1, dzień + 1) + strata przy
przejechaniu z prawej do k (w celu zebrania k), minimize_loss(k + 1, prawa_strona_dzień, dzień + 1) +
strata przy przejechaniu z lewej do k (w celu zebrania k)) gdzie k należy do [lewa, prawa].
Poniższa implementacja zapamiętuje wartości funkcji, których jest co najwyżej n(lewa) * n(prawa) * n(dzień - <= n).
Złożoność obliczeniowa: O(n^4) - mamy n^3 wartości, których obliczenie zajmuje O(n) -> O(n^3 * n) = O(n^4)
Złożoność pamięciowa: O(n^3) - n^3 możliwych wartości funkcji.
'''

from egz1atesty import runtests


def sum_melt_loss(S, left, right, day):
    sum = 0
    for i in range(max(0, left), min(right + 1, len(S))):
        if S[i] - day > 0:
            sum += 1
    return sum


def sum_drive_thought_loss(S, left, right, day):
    sum = 0
    for i in range(left, right + 1):
        sum += max(0, S[i] - day)
    return sum


def minimize_loss(S, left, right, day, fun_vals):
    if left >= right:
        return 0
    if fun_vals[left][right][day] is not None:
        return fun_vals[left][right][day]

    minimal = float('inf')
    for i in range(left, right + 1):
        # jedziemy do i z lewej oraz bierzemy i
        minimal = min(minimal, minimize_loss(S, i + 1, right, day + 1, fun_vals) +
                      sum_drive_thought_loss(S, left, i - 1, day) + sum_melt_loss(S, i + 1, right, day))
        # jedziemy do i z prawej oraz bierzemy i
        minimal = min(minimal, minimize_loss(S, left, i - 1, day + 1, fun_vals) +
                      sum_drive_thought_loss(S, i + 1, right, day) + sum_melt_loss(S, left, i - 1, day))
    fun_vals[left][right][day] = minimal
    return minimal


def snow(S):
    n = len(S)
    sum = 0
    for el in S:
        sum += el
    fun_vals = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]

    return sum - minimize_loss(S, 0, n - 1, 0, fun_vals)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
