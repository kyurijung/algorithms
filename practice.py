def reverseEveryWord(myStr):
    words = myStr.split(" ")
    reversedWords = []
    for word in words:
        reversedWords.append(word[::-1])
    res = " ".join(reversedWords)
    print(res)
    
def newlineToSpace():
    with open("io/sample.txt", "r") as fp:
        lines = fp.read().replace("\n", " ")
    print(lines)

def removeInPlace(myList):
    i = 0
    n = len(myList)
    while i < n:
        if myList[i] > 50:
            del myList[i]
            n -= 1
        else:
            i += 1
    print(myList)

def revDictMapping(myDict):
    resDict = dict(list(zip(myDict.values(),myDict.keys())))
    print(resDict)

def displayDups(myList):
    exists = {}
    i = 0
    n = len(myList)
    while i < n:
        if myList[i] in exists:
            exists[myList[i]] += 1
        else:
            exists[myList[i]] = 1
        i += 1
    resList = [key for key,val in exists.items() if val > 1]
    print(resList)

def filterDict(d,l):
    myDict = {i: d[i] for i in l}
    print(myDict)

def numPattern():
    for i in range(1,6):
        temp = ""
        for j in range(6-i):
            temp += str(i) + " "
        print(temp)

def innerFunc(x,y):
    def innerInnerFunc(x,y):
        return x + y
    z = innerInnerFunc(x,y) + 'Developers'
    print(z)

def modifyNested(myList):
    myList[1][2][2][1] = 3500
    print(myList)

def accessNested(myDict):
    print(myDict['company']['employee']['payable']['increment'])

# 0, 1, 1, 2, 3, 5, 8
# recursive
def nthFib(n):
    if n < 1:
        return 0
    elif n < 3:
        return 1
    else:
        return nthFib(n-1) + nthFib(n-2)
# non-recursive
def fib(n):
    if n < 1:
        return 0
    elif n < 2:
        return 1
    
    prev2, prev1 = 0, 1
    res = 0
    for i in range(2,n+1):
        res = prev2 + prev1
        prev2 = prev1
        prev1 = res
    return res

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

def main():
    # myStr = 'My Name is Jessa'
    # reverseEveryWord(myStr)

    # newlineToSpace()

    # number_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # removeInPlace(number_list)

    # myDict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
    # revDictMapping(myDict)

    # sample_list = [10, 20, 60, 30, 20, 40, 30, 60, 70, 80]
    # displayDups(sample_list)

    # d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}
    # l1 = ['A', 'C', 'F']
    # filterDict(d1,l1)

    # numPattern()

    # x,y = 'Emma','Kelly'
    # innerFunc(x,y)
    
    # list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
    # modifyNested(list1)

    # emp_dict = {
    #     "company": {
    #         "employee": {
    #             "name": "Jess",
    #             "payable": {
    #                 "salary": 9000,
    #                 "increment": 12
    #             }
    #         }
    #     }
    # }
    # accessNested(emp_dict)

    # print(nthFib(6))
    # print(fib(6))

    print(factorial(5))

if __name__ == "__main__":
    main()
