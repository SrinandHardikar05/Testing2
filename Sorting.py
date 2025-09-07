def Selection_Sort(arr):
    n = len(arr)

    for i in range(n-1):
        mini = i
        for j in range(i+1,n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i], arr[mini] = arr[mini], arr[i]

def Bubble_Sort(arr):
    n = len(arr)

    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
            


arr = [13,46,24,52,20,9]
# # Selection_Sort(arr)
Bubble_Sort(arr)
print('Sorted Array:',arr)
