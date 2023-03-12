def radix_sort_string(string_list):
    n = len(string_list)
    max_len = 0
    for str in string_list:
        max_len = max(max_len, len(str))

    for position in range(max_len - 1, -1, -1):
        count = [0 for _ in range(26 + 1)]
        sorted_array = [None for _ in range(n)]
        for str in string_list:
            if len(str) - 1 < position:
                count[0] += 1
            else:
                count[ord(str[position]) - 97 + 1] += 1

        for i in range(1, 27):
            count[i] += count[i - 1]
        for el in range(n - 1, -1, -1):
            if len(string_list[el]) - 1 < position:
                sorted_array[count[0] - 1] = string_list[el]
                count[0] -= 1
            else:
                sorted_array[count[ord(string_list[el][position]) - 97 + 1] - 1] = string_list[el]
                count[ord(string_list[el][position]) - 97 + 1] -= 1

        for i in range(n):
            string_list[i] = sorted_array[i]

    return string_list

print(radix_sort_string(word))