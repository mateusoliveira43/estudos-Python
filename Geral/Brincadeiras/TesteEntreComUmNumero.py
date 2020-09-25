# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 2020

@author: Mateus
"""
# Pede ao usuário que digite um número natural.
#
# Avisa ao usuário quando digita um objeto inválido.
# Caso isso ocorra, pergunta se o usuário quer tentar novamente ou quer 
#encerrar.
# Quando digitado um objeto válido, o programa é encerrado.

import re

def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True

    return False

def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True

    return False
 
def is_number(val):
    return is_int(val) or is_float(val)

while True :
    objeto = input('Digite um número natural: ')
    if objeto.isdigit() :
        pass 
    else :
        print('Um caractere inválido foi digitado.')
        continuar = input('Deseja tentar novamente? Digite s para sim e ' 
                          'qualquer outra tecla para não. ')
        if continuar == 's' :
            continue
        else :
            print('Usuário quis parar.')
            break
    if int(objeto) < 0 :
        print('Um caractere inválido foi digitado.')
        continuar = input('Deseja tentar novamente? Digite s para sim e ' 
                          'qualquer outra tecla para não. ')
        if continuar == 's' :
            continue
        else :
            print('Usuário quis parar.')
            break
    else :
        print('Número válido. ')
        break 
#    try :
#        objeto = int(objeto) 
#        if objeto < 0 :
#            condicao = True
#            raise Exception
#        else :
#            print('Número válido. ')
#            break 
#    except :
#        frase = 'número negativo' if condicao else 'caractere inválido'
#        print(f'Um {frase} foi digitado.')
#        continuar = input('Deseja tentar novamente? Digite s para sim e ' 
#                          'qualquer outra tecla para não. ')
#        if continuar == 's' :
#            continue
#        else :
#            print('Usuário quis parar.')
#            break
        
print('Fim da execução.')













