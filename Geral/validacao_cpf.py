# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 08:55:35 2020

@author: Mateus
"""

# digitos = False
# design = '#'
# frase1 = ' Digite apenas os dígitos do seu CPF em sequência: '
# frase2 = ' Você deve digitar 11 dígitos. '
# frase3 = ' Você digitou um ou mais caracteres inválidos. '
# while not digitos:
def valida_cpf(cpf):
    # cpf_usuario = input(f'{frase1:#>77}')
    cpf_usuario = str(cpf)
    if len(cpf_usuario) != 11:
        # print(f'{frase2:#^109}')
        # continue
        return False
    try:
        checagem_cpf = cpf_usuario[:9]
        cpf_usuario = int(cpf_usuario)
        # digitos = True
        # break
        soma1 = 0
        for e, i in enumerate(range(10, 1, -1)):
            soma1 += i * int(checagem_cpf[e])
        c1 = 11 - (soma1 % 11)
        digito1 = str(c1) if c1 <= 9 else str(0)
        checagem_cpf += digito1
        soma2 = 0
        for e, i in enumerate(range(11, 1, -1)):
            soma2 += i * int(checagem_cpf[e])
        c2 = 11 - (soma2 % 11)
        digito2 = str(c2) if c2 <= 9 else str(0)
        checagem_cpf += digito2
        if checagem_cpf == str(cpf_usuario):
            return True
        else:
            return False
    except ValueError:
        # print(f'{frase3:#^109}')
        return False
# design = '#'
# print(f'{design:#^109}')
# frase = ' Vamos verificar se você digitou corretamente seu CPF. '
# print(f'{frase:#^109}')
# print(f'{design:#^109}')

# soma1 = 0
# for e, i in enumerate(range(10, 1, -1)):
#     soma1 += i * int(checagem_cpf[e])
# c1 = 11 - (soma1 % 11)
# digito1 = str(c1) if c1 <= 9 else str(0)
# checagem_cpf += digito1
# soma2 = 0
# for e, i in enumerate(range(11, 1, -1)):
#     soma2 += i * int(checagem_cpf[e])
# c2 = 11 - (soma2 % 11)
# digito2 = str(c2) if c2 <= 9 else str(0)
# checagem_cpf += digito2
# if checagem_cpf == str(cpf_usuario):
#     print(f'{design:#^109}')
#     frasev = ' Você digitou corretamente seu CPF. '
#     print(f'{frasev:#^109}')
#     print(f'{design:#^109}')
# else:
#     print(f'{design:#^109}')
#     frasei = ' Você não digitou corretamente seu CPF. '
#     print(f'{frasei:#^109}')
#     print(f'{design:#^109}')
