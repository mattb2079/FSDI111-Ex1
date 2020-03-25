#method on the top
def separator():
    print(40 * '-')

def menu():
    print(5 * '\n')
    separator()
    print(' Welcome to PyCalc')
    separator()
    print('[1] - Add')
    print('[2] - Subtract')
    print('[3] - Multiply')
    print('[4] - Divide')
    print('[x] - Exit')



# instruction on the bottom


opc = ''
while(opc != 'x'):
    menu()
    opc = input('Select an option: ')
    if(opc == 'x'):
        break #break finish with the loop

    num1 = float(input ('First number: '))
    num2 = float(input ('Second number: '))

    if (opc == '1'):
        res = num2 + num1
        print('Sum = ' + str(res))
    elif (opc == '2'):
        res = num1 - num2
        print('Difference = ' + str(res))
    elif (opc == '3'):
        res = num2 * num1
        print('Product = ' + str(res))
    elif (opc == '4'):
        if(num2 == 0):
            print('Dividing by 0 will destroy the universe')
        else:
            res = num1 / num2
            print('Quotient = ' + str(res))
    input('Press ENTER to continue...')

print ('Thank you!!')