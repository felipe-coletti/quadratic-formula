def getValues(equation):
    for i in range(len(equation)):
        if i > 0 and equation[i] == '-' and equation[i - 1] != ' ':
            equation = equation.replace(equation[i], ' -')
        
        if not equation[i].isnumeric() and equation[i] != 'x' and equation[i] != '-' and equation[i] != ' ':
            equation = equation.replace(equation[i], '/')
    
    while '- ' in equation:
        equation = equation.replace('- ', '-')
    
    for i in range(len(equation)):
        if equation[i] == ' ':
            equation = equation.replace(equation[i], '/')
    
    while '//' in equation:
        equation = equation.replace('//', '/')
    
    equation = equation.split('/')
    
    result = ''
    
    addedA = addedB = addedC = False
    
    for i in range(len(equation)):
        if 'x²' in equation[i]:
            if len(result) > 0:
                result += '/'
            if len(equation[i].replace('x²', '')) == 0:
                result += '1'
            else:
                result += equation[i].replace('x²', '')
            addedA = True
    
    if addedA == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    for i in range(len(equation)):
        if 'x' in equation[i] and not '²' in equation[i]:
            if len(result) > 0:
                result += '/'
            if len(equation[i].replace('x', '')) == 0:
                result += '1'
            else:
                result += equation[i].replace('x', '')
            addedB = True
    
    if addedB == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    for i in range(len(equation)):
        if not 'x' in equation[i]:
            if len(result) > 0:
                result += '/'
            result += equation[i]
            addedC = True
    
    if addedC == False:
        if len(result) > 0:
            result += '/'
        result += '0'
    
    result = result.split('/')
    
    return result


def findSolution(a, b, c):
    if b == 0 or c == 0:
        print('A equação é incompleta.')
    
    discriminant = b**2 - 4 * a * c
    
    print('{}² - 4 . {} . {}'.format(b, a, c))
    
    firstPart = b**2
    secondPart = - 4 * a * c
    
    if secondPart < 0:
        print('{} - {}'.format(firstPart, secondPart * -1))
    else:
        print('{} + {}'.format(firstPart, secondPart))
    
    print(discriminant)
    
    if discriminant > 0:
        if b < 0:
            print('\n{} ± √{} / 2 . {}'.format(b * -1, discriminant, a))
        else:
            print('\n-{} ± √{} / 2 . {}'.format(b, discriminant, a))
        
        x1 = (-b + (discriminant**(1/2))) / (2 * a)
        x2 = (-b - (discriminant**(1/2))) / (2 * a)
    
        print('\nx = {:.2f}'.format(x1))
        print('x = {:.2f}'.format(x2))
    elif discriminant == 0:
        if b < 0:
            print('\n{} / 2 . {}'.format(b * -1, a))
        else:
            print('\n-{} / 2 . {}'.format(b, a))
        
        x = -b / (2 * a)
        
        print('\nx = {:.2f}'.format(x))
    else:
        print('\nEssa equação não apresenta raízes reais.')


quadraticEquation = input('Digite uma equação de 2ºgrau: ')

values = getValues(quadraticEquation)

a = int(values[0])
b = int(values[1])
c = int(values[2])

if a == 0:
    print('Equação inválida.')
else:
    findSolution(a, b, c)
