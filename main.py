from operator import truediv


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

def sumX():
    #empty list
    #append to list while true
    #give sum
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
    start = True
    while start == True:
        print("Hello World")
        #rest of code goes here
        sumX()

        #this happens when code ends
        print("Continue?(Y/N)")
        cont = input()
        if cont != "Y":
            start = False
            print("Goodbye World!")

if __name__ == "__main__":
    main()
