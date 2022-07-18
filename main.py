from audioop import mul


def test():
    print("Test")

def sum(n1, n2):
    print(f"Sum of x + y is: {n1+n2}")

def minus(n1, n2):
    print("Minus of x and y is: ")
    print(n1 - n2)

def multiply(n1, n2):
    print("Multiplication of both numbers are: ")
    print(n1 * n2)

def division(n1, n2):
    print("Division of both numbers are: ")
    print(n1 / n2)

def main():
    #what = "Ben"
    #print(f'Hello {what}')
    sum(5,7)

if __name__ == "__main__":
    main()
