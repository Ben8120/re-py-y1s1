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

def main():
    start = True
    while start == True:
        print("Hello World")
        print("Continue?(Y/N)")
        cont = input()
        if cont == "Y":
            start = True
        elif cont == "N":
            start = False
        else:
            print("??")

if __name__ == "__main__":
    main()
