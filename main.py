def test():
    print("Test")

def sum(n1, n2):
    print(f"Sum of both numbers are: {n1+n2}")

def minus(n1, n2):
    print(f"Minus of both numbers are: {n1-n2}")

def multiply(n1, n2):
    print(f"Multiplication of both numbers are: {n1*n2}")

def division(n1, n2):
    print(f"Division of both numbers are: {n1/n2}")

def listExample():
    thisList = ["apple", "orange", "mango"]
    for currentList in thisList:
        print(currentList)
    thisList.append("starfruit")
    print(thisList)

#enhance this to continue entering numbers until a non-number is added
def sumX():
    sumList = []
    total = 0
    cont = True
    print("Enter a number")
    while cont == True:
        sumList.append(int(input()))
        print("Add another number?(Y)")
        x = input()
        if x != "Y":
            cont = False
    print(sumList)
    for num in sumList:
        total+=num
    print(f'sum of these numbers are: {total}')

def main():
    task = 0
    start = True
    while start == True:
        print('-------------------------------------------------------')
        print("Hello World! Welcome to Ben's pointless python program!")
        print('-------------------------------------------------------')
        print('What would you like to do?\n 1. Sum X (add as much number as possible)\n 2. Minus two numbers')
        print(' 0. exit program')
        #rest of code goes here
        task = int(input())
        if task == 1:
            sumX()
        if task == 2:
            print("Enter two numbers:")
            num1 = int(input())
            num2 = int(input())
            minus(num1, num2)
        
        if task == 0:
            print('Goodbye World!')
            break
        else:
            print("What is that?")

        #this happens when code ends
        print("Continue?(Y/N)")
        cont = input()
        if cont != "Y":
            start = False
            print("Goodbye World!")

if __name__ == "__main__":
    main()
