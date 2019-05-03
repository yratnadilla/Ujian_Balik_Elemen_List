def reverse(list):
    reversedList = []
    i = len(list) - 1

    while i >= 0 :
        reversedList.append(list[i]) 
        i -= 1
    return reversedList

print(reverse([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(reverse(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(reverse(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))
