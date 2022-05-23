while True:
    print("Select an operation to perform: ")
    print('1. Add')
    print('2. sub')
    print('3. multi')
    print("press (e) to exit")

    def add(x, y):
        return x+y
    def sub(x, y):
        return x-y
    def mul(x, y):
        return x*y

    operation = int(input("Enter operation number: "))
    if operation == "e":
        break


    elif  operation == 1:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The sum is {}".format(add(num1, num2)))

    elif operation == 2:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The substraction is {}".format(sub(num1, num2)))

    elif operation == 3:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        print("The multiplication is {}".format(mul(num1, num2)))
    else:
        print("Enter the correct operation number")