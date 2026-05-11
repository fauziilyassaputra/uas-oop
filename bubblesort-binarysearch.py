def bubble_sort(arr: list[int]) -> list[int]:
    length = len(arr)
    for i in reversed(range(length)):
        swapped = False
        for j in range(i):
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if not swapped:
            break
    return arr

"""
i = 4
[4,7,5,2,1] => j= 0
[4,5,7,2,1] => j = 1
[4,5,2,7,1] => j = 2
[4,5,2,1,7] => j = 3


i = 3
[4,5,2,1,7] j = 0
[4,2,5,1,7] j = 1
[4,2,1,5,7] j = 2


i = 3
[4,2,1,5,7] 
[2,4,1,5,7] j = 0
[2,1,4,5,7] j = 1 
[2,1,4,5,7] j = 2

i = 2
[1,2,4,5,7] j = 0
[1,2,4,5,7] j = 1


"""


def binary_search(data_sorted: list[int], item: int) -> int:
    left = 0
    right = len(data_sorted) - 1

    while left <= right:
        midPoint = left + (right - left) // 2
        current_item = data_sorted[midPoint]
        if current_item == item:
            return midPoint
        elif item < current_item:
            right = midPoint - 1
        else:
            left = midPoint + 1
    return - 1
    

kumpulan_angka = [9,5,7,3,1,2,4]
urutkan_angka = bubble_sort(kumpulan_angka)
print(urutkan_angka)
cari_angka = 2
print(f"indeks angka: {cari_angka} adalah ",binary_search(kumpulan_angka, cari_angka))