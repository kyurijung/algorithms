def linearSearch(arr,x):
    # src: https://www.geeksforgeeks.org/linear-search/
    # O(n) and O(1)
    for i in range(len(arr)):
        if arr[i] == x:
            print(i)

def binarySearch(arr,x):
    # src: https://www.geeksforgeeks.org/binary-search/
    # O(log n) and O(1)
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            print(mid)
            return
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    print("-1")

def main():
    oddLenArr = [2, 3, 4, 10, 40, 24, 9]
    print(oddLenArr)
    evenLenArr = [2, 3, 4, 10, 24, 9]
    # print("Original Array: ",evenLenArr)

    # linearSearch(oddLenArr,10)

    binarySearch(oddLenArr,11)

if __name__ == "__main__":
    main()
