from math import sqrt

# solicita a equação de 2ºgrau que será calculada
equation = input('Digite a equação de 2ºgrau: ')


# remove os caracteres que não serão utilizados
def clear(information):
    for i in range(len(information)):
        if not information[i].isnumeric() and information[i].isalpha() or information[i] == '²' or information[i] == '=':
            information = information.replace(information[i], '/')
    while '//' in information:
        information = information.replace('//', '/')

    information = information.split('/')

    return information


# armazena os valores que serão utilizados
numbers = clear(equation)

# verifica se a equação é válida
if len(numbers) < 3 or numbers[0] == 0 or numbers[1] == 0 or numbers[2] == 0:
    print('Equação inválida.')
else:
    # calulca a equação
    a = int(numbers[0])
    b = int(numbers[1])
    c = int(numbers[2])

    delta = b**2 - 4 * a * c

    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)

    # exibe o resultado
    print('{}² - 4 . {} . {}'.format(b, a, c))

    secondPart = - 4 * a * c

    if secondPart < 0:
        secondPart *= - 1
        print('{} - {}'.format(b**2, secondPart))
    else:
        print('{} + {}'.format(b**2, secondPart))

    print(delta)

    if delta > 0:
        if b < 0:
            b *= - 1
            print('\n{} +- √{} / 2 . {}'.format(b, delta, a))
        else:
            print('\n-{} +- √{} / 2 . {}'.format(b, delta, a))

        print('\nx1 = {:.0f}'.format(x1))
        print('x2 = {:.0f}'.format(x2))
