# src: https://pynative.com/python-if-else-and-for-loop-exercise-with-solutions/

def ex1():
    count = 1
    while count < 11:
        print(count)
        count += 1

def ex2():
    for i in range(1,6):
        myStr = ""
        for z in range(1,i+1):
            myStr += str(z)
        print(myStr)

def ex3():
    sum = 0
    for i in range(11):
        sum += i
    print(sum)

def ex4():
    for i in range(1,11):
        print(i*2)

def ex5():
    numbers = [12, 75, 150, 180, 145, 525, 50]
    for num in numbers:
        if num > 500:
            break
        elif num > 150:
            continue
        elif num % 5 == 0:
            print(num)

def ex6():
    num = 75869
    count = 0
    while num != 0:
        num = num // 10
        count += 1
    print(count)

def ex7():
    for i in range(5,0,-1):
        myStr = ""
        for j in range(i,0,-1):
            myStr += str(j)
        print(myStr)

def ex8():
    list1 = [10, 20, 30, 40, 50]
    for i in range(len(list1)-1,-1,-1):
        print(list1[i])

def ex9():
    for i in range(-10,0,1):
        print(i)

def ex10():
    for i in range(5):
        print(i)
    else:
        print("DONE!")

def ex11():
    for i in range(25,51):
        if i > 1:
            for j in range(2,i):
                if i % j == 0:
                    break
            else:
                print(i)

def ex12():
    myArr = [0,1]
    for i in range(2,10):
        myArr.append(myArr[i-2] + myArr[i-1])
    print(myArr)
        
def ex13():
    res = 1
    for i in range(1,6):
        res = res * i
    print(res)

def ex14():
    num = 76542
    reversedNum = 0
    while num != 0:
        digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num = num // 10
    print(reversedNum)

def ex15():
    my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    for i in range(1,len(my_list),2):
        print(my_list[i])

def ex16():
    myArr = []
    for i in range(1,7):
        cubed = i ** 3
        myArr.append(cubed)
        # print(f"{i}: {cubed}")
    print(myArr)
    return myArr

def ex17():
    base = 2
    res = 0
    for i in range(5):
        res += base
        base = base * 10 +2
    print(res)

def ex18():
    for i in range(5):
        myStr = ""
        for j in range(i+1):
            myStr += "* "
        print(myStr)
    for i in range(4,0,-1):
        myStr = ""
        for j in range(i):
            myStr += "* "
        print(myStr)

def ex19():
    sentences = ["tom like alice","alice like to play","jerry and tom like to play"]
    query = ["jerry tom","alice"]

    for q in query:
        keys = q.split()
        printStat = ""
        for i in range(len(sentences)):
            # print("MY SENT: ",sentences[i])
            flag = True
            for key in keys:
                # print(key)
                if sentences[i].count(key) < 1:
                    # print("NOT FOUND")
                    flag = False
                    break
            if not flag and not printStat:
                # print("NO QUERY")
                printStat = "-1"
                # print(printStat)
            elif flag:
                # print("ADDING QUERY")
                if printStat == "-1":
                    printStat = str(i)
                else:
                    printStat += str(i) + " "
                # print(printStat)
        print(printStat)

def ex20():
    def addCourse(mySet,myDict,course_id,course_name,capacity):
        if course_id not in mySet and course_name not in mySet:
            mySet.add(course_id)
            mySet.add(course_name)
            myDict[course_id] = [course_name,capacity]
        return myDict
    
    mySet = set()
    myDict = {}
    addCourse(mySet,myDict,1,"Science",10)
    addCourse(mySet,myDict,2,"Science",15)
    addCourse(mySet,myDict,3,"Interdis Sci-Fi",10)
    addCourse(mySet,myDict,2,"Geeky Squad",8)
    print(myDict)

def ex21():
    myArr = [
        [' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ']
    ]
    for i in range(5):
        myArr[i][i] = 'X'
        myArr[i][5-i-1] = 'X'
    return myArr

def main():
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex5()
    # ex6()
    # ex7()
    # ex8()
    # ex9()
    # ex10()
    # ex11()
    # ex12()
    # ex13()
    # ex14()
    # ex15()
    ex16()
    # ex17()
    # ex18()
    # ex19()
    # ex20()
    # ex21()

if __name__ == "__main__":
    main()
