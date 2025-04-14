def bubbleSort(arr):
    # src: https://www.geeksforgeeks.org/bubble-sort/
    # O(n^2) and O(1)
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    print(arr)

def insertionSort(arr):
    # src: https://www.geeksforgeeks.org/insertion-sort/
    # O(n^2) and O(1)
    for i in range(1,len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    print(arr)

def selectionSort(arr):
    # src: https://www.geeksforgeeks.org/selection-sort/
    # O(n^2) and O(1)
    for i in range(len(arr)):
        minIdx = i
        for j in range(i+1,len(arr)):
            if arr[minIdx] > arr[j]:
                minIdx = j
        arr[i],arr[minIdx] = arr[minIdx],arr[i]
    print(arr)

def quickSort(arr,low,high):
    # src: https://www.geeksforgeeks.org/quick-sort/
    # src: https://www.youtube.com/watch?v=Vtckgz38QHs
    # Avg: O(n log n) Worst: O(n^2) and O(1)
    def partition(arr,low,high):
        pivot = arr[high]
        i = low-1
        for j in range(low,high):
            if arr[j] <= pivot:
                i += 1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    if low < high:
        piv = partition(arr,low,high)
        quickSort(arr,low,piv-1)
        quickSort(arr,piv+1,high)

def mergeSort(arr):
    # src: https://www.geeksforgeeks.org/merge-sort/
    # O(n log n) and O(1)
    print(arr)

def bucketSort(arr):
    # src: https://www.geeksforgeeks.org/bucket-sort-2/
    # O(n^2) and O(n+k)
    print(arr)

def countingSort(arr):
    # src: https://www.geeksforgeeks.org/counting-sort/
    # O(n+k) and O(n+k)
    print(arr)

def radixSort(arr):
    # src: https://www.geeksforgeeks.org/radix-sort/
    # O(d(n+b)) and O(n+b)
    print(arr)

def heapSort(arr):
    # src: https://www.geeksforgeeks.org/heap-sort/
    # O(n log n) and Recursive: O(log n) Iterative: O(n) 
    print(arr)

def main():
    oddLenArr = [64, 34, 25, 12, 22, 11, 90]
    print(oddLenArr)
    evenLenArr = [64, 34, 25, 12, 22, 11]
    # print("Original Array: ",evenLenArr)

    # bubbleSort(oddLenArr)

    # insertionSort(oddLenArr)

    # selectionSort(oddLenArr)

    quickSort(oddLenArr,0,len(oddLenArr)-1)
    print(oddLenArr)

    # mergeSort(oddLenArr)

    # bucketSort(oddLenArr)

    # countingSort(oddLenArr)

    # radixSort(oddLenArr)

    # heapSort(oddLenArr)




if __name__ == "__main__":
    main()
