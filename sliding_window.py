# Use: Array, String, Sub Array, Sub String, Largest Sum, Maximum Sum, Minimum Sum

def naiveAlgorithm(arr,k):
    # src: https://www.geeksforgeeks.org/window-sliding-technique/
    # O(n*k) and O(1)
    maxSum = 0
    for i in range(len(arr)-k+1):
        currSum = 0
        for j in range(k):
            currSum += arr[i+j]
        maxSum = max(currSum,maxSum)
    print(maxSum)

def main():
    arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
    k = 4

    naiveAlgorithm(arr,4)

if __name__ == "__main__":
    main()
