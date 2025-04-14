# src: https://pynative.com/python-input-and-output-exercise/

def ex1():
    num1 = int(input("Write your first number: "))
    num2 = int(input("Write your second number: "))
    res = num1*num2
    print(f"Your numbers multiplied: {res}")

def ex2():
    print('Name','Is','James',sep="**")

def ex3():
    num = 8
    print("%o" % num)

def ex4():
    num = 458.541315
    print("%.2f" % num)

def ex8():
    totalMoney = 1000
    quantity = 3
    price = 450
    statement = "I have {0} dollars so I can buy {1} football for {2:.2f} dollars."
    print(statement.format(totalMoney,quantity,price))

# src: https://holypython.com/intermediate-python-exercises/exercise-1-python-format-method/

def exA():
    name = "Kyuri"
    myStr = "Hello, my name is {}".format(name)
    print(myStr)

def exB():
    print("{}".format(1))

def exC():
    print("{}, {}, {}".format(1,2,3))

def exD():
    myStr = "One year has {} months, {} weeks and {} days.".format(12,52,365)
    print(myStr)

def exF():
    John = 75
    Ann = 80
    Ally = 60
    myStr = "Scores were as following: John: {}, Ann: {}, Ally: {}"
    myStr = myStr.format(John, Ann, Ally)
    print(myStr)

# src: https://www.freecodecamp.org/news/2f-in-python-what-does-it-mean/

def floats():
    floatNumber = 1.9876
    print("%f" % floatNumber) # 1.987600
    
def floorFloat():
    floatNumber = 1.9876
    print("%d" % floatNumber) # 1

def decimalPlaces():
    floatNumber = 1.9876
    y = "{:.2f}".format(floatNumber)
    print(y) # 1.99
    print("%.2f" % floatNumber) # 1.99
    print("%.1f" % floatNumber) # 2.0

def main():
    # ex1()
    # ex2()
    # ex3()
    # ex4()
    # ex8()
    # exA()
    # exB()
    # exC()
    # exD()
    # exF()
    
    floats()
    floorFloat()
    decimalPlaces()

if __name__ == "__main__":
    main()
