import random
def comb_sort(arr):
    per = 0
    por = 0
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False
    while not sorted:
        gap = int(gap / shrink)
        if gap > 1:
            sorted = False
        else:
            gap = 1
            sorted = True

        i = 0
        while i + gap < n:
            por+=1
            if arr[i] > arr[i + gap]:
                per+=1
                swap(i, i + gap)
                sorted = False
            i = i + 1
   
    return por,per
n = int(input(" задайте розмір масиву: "))
array = list(range(1,n+1))
random.shuffle(array)
print("початковий: ",array)
comb_sort(array)
print("відсортований: ",array)

