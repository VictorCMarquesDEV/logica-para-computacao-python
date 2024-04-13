"""

Programa que verifica se a expressão lógica é válida.

Proposições:
De A até Z, exceto V e F

Verdade:
V
F

Pontuação:
(
)

Conectivos:
~        NEGADO
&        AND
|        OR
>        SE, IMPLICA
=        SE, SOMENTE SE

"""

import string

print(f'\033[0;49;32m-=-' * 20)
print(f'|       Verificar se a expressão lógica é válida     |')
print(f'-=-' * 20, '\033[m')

prop1 = list(input(f'Digite a expressão lógica: '))
alf = list(string.ascii_uppercase)
parent = list()
prop2 = list()


# Verifica a ordem entre os parênteses
for letra in prop1:
    if letra == '(':
        parent.append('(')
    elif letra == ')':
        if parent:
            parent.pop()
        else:
            print("A expressão não é válida! Parênteses desbalanceados.")
            exit()
if parent:
    print("A expressão não é válida! Parênteses desbalanceados.")
    exit()


# Cria uma nova lista sem parênteses
for letra in prop1:
    if letra != '(' and letra != ')':
        prop2.append(letra)
prop1.clear()


# Verifica a ordem entre as proposições e conectivos
i = 0
ver = False
while prop2.__len__() != 0:
    if (i % 2) == 0 and ver == False and prop2[0] in alf:
        del prop2[0]
        i += 1
        ver = True
    elif (i % 2) == 1 and ver == True and (prop2[0] == '|' or prop2[0] == '&' or prop2[0] == '>' or prop2[0] == '='):
        del prop2[0]
        i += 1
        ver = False
    elif prop2[0] == '~':
        if prop2[1] == '~':
             del prop2[0]
        elif prop2[1] in alf:
            del prop2[0]
        else:
            print(f'A expressão não é válida!')
            exit()
    else:
        print(f'A expressão não é válida!')
        exit()

if (i % 2) == 1:
    print(f'A expressão é válida!')
    exit()
else:
    print(f'A expressão não é válida!')
    exit()
