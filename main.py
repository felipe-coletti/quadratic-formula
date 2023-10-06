equation = input('Digite uma equação de 2ºgrau: ')


def clear(information):
    for i in range(len(information)):
        if not information[i].isnumeric() and information[i] != 'x' and information[i] != '-' and information[i] != ' ':
            information = information.replace(information[i], '/')
    while '- ' in information:
        information = information.replace('- ', '-')
    for i in range(len(information)):
        if information[i] == ' ':
            information = information.replace(information[i], '/')
    while '//' in information:
        information = information.replace('//', '/')
    
    information = information.split('/')
    
    result = ''
    
    addedA = addedB = addedC = False
    
    for i in range(len(information)):
        if 'x²' in information[i]:
            if len(result) > 0:
                result += '/'
            result += information[i].replace('x²', '')
            addedA = True
    if addedA == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    for i in range(len(information)):
        if 'x' in information[i] and not '²' in information[i]:
            if len(result) > 0:
                result += '/'
            result += information[i].replace('x', '')
            addedB = True
    if addedB == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    for i in range(len(information)):
        if not 'x' in information[i]:
            if len(result) > 0:
                result += '/'
            result += information[i]
            addedC = True
    if addedC == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    result = result.split('/')
    
    return result


numbers = clear(equation)

a = int(numbers[0])
b = int(numbers[1])
c = int(numbers[2])

if a == 0:
    print('Equação inválida.')
else:
    if len(numbers) < 3 or b == 0 or c == 0:
        print('A equação é incompleta.')
    
    delta = b**2 - 4 * a * c
    
    x1 = (-b + (delta**(1/2))) / (2 * a)
    x2 = (-b - (delta**(1/2))) / (2 * a)
    
    print('{}² - 4 . {} . {}'.format(b, a, c))
    
    firstPart = b**2
    secondPart = - 4 * a * c
    
    if secondPart < 0:
        secondPart *= -1
        print('{} - {}'.format(firstPart, secondPart))
    else:
        print('{} + {}'.format(firstPart, secondPart))
    
    print(delta)
    
    if delta > 0:
        if b < 0:
            b *= -1
            print('\n{} ± √{} / 2 . {}'.format(b, delta, a))
        else:
            print('\n-{} ± √{} / 2 . {}'.format(b, delta, a))
    
        print('\nx1 = {:.0f}'.format(x1))
        print('x2 = {:.0f}'.format(x2))
    else:
        print('\nEssa equação não apresenta raízes reais.')
