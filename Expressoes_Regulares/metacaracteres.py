# Meta Caracteres . ^ $ * + ? { } [ ] \ | ( )
# \ : Caractere de escape
# | : OU
# . : Qualquer caractere (com exceção da quebra de linha)
# [] : Conjunto de caracteres, [a-zA-Z0-9] : range
# * : 0 ou ilimitada repetições
# + : 1 ou ilimitada repetições
# ? : 0 ou 1 repetições
# {N} : N repetições
# {min, max} : min à max repetições
# () : Grupo de caracteres, () \1 : retrovisor, ?: ignorar grupo
# ^ : Começa com
# $ : Termina com
# [^a-z] : Negação
# \w : [a-zA-Z0-9À-ú], \W negação
# \d : [0-9], \D negação
# \s : espaço, \S negação
# \b : borda, \B negação
#
# re.A : ASCII
# re.I : IGNORECASE
# re.M : Multiline
# re.S : Dotall

# https://regex101.com/

import re
from pprint import pprint

# texto = '''
# João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
# Maria era o nome dela.
# Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
# maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
# domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
# pão de queijo.
# Não canso de ouvir a Maria:
# "Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
# jã
# '''

# print(re.findall(r'[Jj]oão|.aria', texto))
# print(re.findall(r'[a-zA-Z]oão|.aria', texto))
# print(re.findall(r'ad.....', texto))
# print(re.findall(r'jOão|MaRia', texto, flags=re.I))

# print(re.findall(r'jo+ão+', texto, flags=re.I))
# print(re.findall(r'jo?ão?', texto, flags=re.I))
# print(re.findall(r'jo{1}ão{1}', texto, flags=re.I))
# print(re.findall(r'jo{,1}ão{,1}', texto, flags=re.I))
# print(re.findall(r'jo{1,}ão{1,}', texto, flags=re.I))
# print(re.findall(r'jo{1,9}ão{1,99}', texto, flags=re.I))

# texto2 = 'João ama ser amado'
# print(re.findall(r'ama[do]*', texto2, flags=re.I))

# texto3 = '''
# <p>Frase 1</p> <p>Eita</p> <p>Qualquer Frase</p> <div></div>
# '''
# print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto3))
# pprint(re.findall(r'(<([pdiv]{1,3})>.*?<\/\2>)', texto3))
# pprint(re.findall(r'<(?P<tag>[pdiv]{1,3})>(.*?)<\/(?P=tag)>', texto3))

# print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 "\3" \4', texto3))

# cpf = '147.852.963-12'
# pprint(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf))
# pprint(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))
# pprint(re.findall(r'[^a-z0-9]+', cpf))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ú]+', texto))
# print(re.findall(r'\w+', texto))
# print(re.findall(r'\W+', texto))
# print(re.findall(r'\W+', texto, flags=re.A))
# pprint(re.findall(r'\d+', texto))
# pprint(re.findall(r'\D+', texto))
# print(re.findall(r'\s+', texto))
# print(re.findall(r'\S+', texto))
# print(re.findall(r'\be\w+', texto, flags=re.I))
# print(re.findall(r'\w+e\b', texto, flags=re.I))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))

# texto4 = '''
# 131.768.460-53 a
# 055.123.060-50
# 955.123.060-90
# '''

# pprint(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto4))
# pprint(re.findall(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', texto4, flags=re.M))

# texto5 = 'O João gosta de folia \n E adora ser amado'
# print(re.findall(r'^o.*o$', texto5, flags=re.I | re.S))

# texto6 = '''
# ONLINE  192.168.0.1 GHIJK active
# OFFLINE  192.168.0.2 GHIJK inactive
# OFFLINE  192.168.0.3 GHIJK active
# ONLINE  192.168.0.4 GHIJK active
# ONLINE  192.168.0.5 GHIJK inactive
# OFFLINE  192.168.0.6 GHIJK active
# '''

# Positive lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto6))

# Negative lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto6))

# pprint(re.findall(r'(?=.*inactive).+', texto6))
# pprint(re.findall(r'(?=.*[^in]active).+', texto6))

# Positive lookbehind
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto6))

# Negative lookbehind
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto6))

# cpf = '025.258.963-10'
# cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')
# print(cpf_reg_exp.search(cpf))

# ip_reg_exp = re.compile(r'''
#     ^
#     (?:
#         (?:
#             25[0-5]| # 250-255
#             2[0-4][0-9]| # 200-249
#             1[0-9]{2}| # 100-199
#             [1-9][0-9]| # 10-99
#             [0-9] # 0-9
#         )
#         \.
#     ){3}
#     (?:
#         25[0-5]| # 250-255
#         2[0-4][0-9]| # 200-249
#         1[0-9]{2}| # 100-199
#         [1-9][0-9]| # 10-99
#         [0-9] # 0-9
#     )
#     $
# ''', flags=re.X)

# for i in range(301):
#     ip = f'{i}.{i}.{i}.{i}'
#     print(ip, ip_reg_exp.findall(ip))

# test_str = ('''
#     698.547.520-54
#     060.235.190-16
#     683.134.960-96
#     899.344.730-62
#     103.778.870-21
#     721.478.580-30
#     366.310.090-14
#     794.289.350-26
#     190.259.410-01
#     000.000.000-01
#     900.000.000-00

#     000.000.000-00
#     111.111.111-11
#     222.222.222-22
#     333.333.333-33
#     444.444.444-44
#     555.555.555-55
#     666.666.666-66
#     777.777.777-77
#     888.888.888-88
#     999.999.999-99
# ''')

# regex = r'^(?!(\d)\1{2}\.\1{3}\.\1{3}-\1{2})\d{3}\.\d{3}\.\d{3}-\d{2}$'

# telefone = '''
# (21) 9 8852-5214
# (11)9955-1231
# (35) 9 9975-4521
# (31) 3851-2587
# 9 8571-5213
# 1234-5647
# '''

# regex = r"^(\(\d{2}\)\s?)?(9\s?)?\d{4}-?\d{4}$"
