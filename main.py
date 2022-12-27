def greedisgood():
    print('Hi, this is simple calculator,\nYou can use following actions: \n    +\n     -\n     *\n     /\n')
    firstNumber = int(input('First number: '))
    operation = input('Choose operation: ')
    secondNumber = int(input('Second number: '))
    if operation == '+':
        print('Result: ', firstNumber+secondNumber)
    elif operation == '-':
        print('Result: ', firstNumber-secondNumber)
    elif operation == '*':
        print('Result: ', firstNumber*secondNumber)
    elif operation == '/':
        print('Result: ', round(firstNumber/secondNumber),3)
    else:
        print('Please, use available operation.')




if __name__ == '__main__':
    greedisgood();

# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
