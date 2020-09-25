# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:18:43 2020

@author: Mateus
"""

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

a = input('Digite um número inteiro: ') # str

if not is_number(a) :
    print('Você usou algum caractere inválido, tente novamente.')
else :
    a = float(a)    
    if int(a) != a : 
        print('Você digitou um número real, tente novamente.')
    else :
        if a % 2 :
            print('O número digitado é ímpar.')
        else :
            print('O número digitado é par.')
