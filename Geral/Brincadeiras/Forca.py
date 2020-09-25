# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 18:19:34 2020

@author: Mateus
"""

design = '%'; espacamento = 90; largura = 109
espaco = ' '; espaco = f'{espaco:^{espacamento}}'
bemvindo = ' Bem-vindo ao Jogo da Forca '  # bemvindo = f'{bemvindo:^{espacamento}}'
versao = f' - versão 1.00 - '  # versao = f'{versao:^{espacamento}}'
atualizado = f'  Atualizado em: 04/04/2020'; atualizado = f'{atualizado:<{espacamento}}'
produzido = f'  Produzido por: Mateus Souza Oliveira, Bacharel em Matemática - UFSC' 
produzido = f'{produzido:<{espacamento}}'
regras1 = '  Cada palavra do jogo tem uma dica. Digite uma letra por vez. Cada letra digitada  '
regras2 = '  aparecerá no banco de letras. Se a letra digitada pertencer a palavra do jogo (e já  '
regras3 = '  não tiver sido digitada), ela aparecerá, nas devidas posições, na sombra da palavra.  '
regras4 = '  Caso contrário, você perderá uma tentativa. Se você digitar todas as letras da palavra  '
regras5 = '  do jogo, você ganha. Caso contrário, você perde.  ' 
regras1 = f'{regras1:<{espacamento}}'; regras2 = f'{regras2:<{espacamento}}' 
regras3 = f'{regras3:<{espacamento}}'; regras4 = f'{regras4:<{espacamento}}'
regras5 = f'{regras5:<{espacamento}}'

#################################
# - Estrutura Gráfica Inicial - #
#################################

print(f'{design:{design}^{largura}}') 
print(f'{bemvindo:{design}^109}')
print(f'{versao:{design}^109}')
print(f'{design:{design}^{largura}}')
print(f'{atualizado:{design}^109}')
print(f'{produzido:{design}^109}')
print(f'{design:{design}^{largura}}')
print(f'{" - COMO JOGAR - ":{design}^{largura}}')
print(f'{design:{design}^{largura}}')
print(f'{regras1:{design}^{largura}}')
print(f'{regras2:{design}^{largura}}')
print(f'{regras3:{design}^{largura}}')
print(f'{regras4:{design}^{largura}}')
print(f'{regras5:{design}^{largura}}')
print(f'{design:{design}^{largura}}')
print(f'{" - BOA SORTE - ":{design}^{largura}}')
# print(f'{design:{design}^{largura}}')

########################
# - Iniciando o Jogo - #
########################

# forca = input('Insira a palavra do jogo: ')
# dica = input('Insira a dica da palavra do jogo: ')

# TODO : importar algum banco de dados com as palvaras e suas dicas.
forca = 'papagaio'
dica = f'  Dica: é uma ave.'; dica = f'{dica:<{espacamento}}'

sombra = ''
qtd_letras = 0
for letra in forca:
    if letra == ' ':
        sombra += ' '
    elif letra == '-':
        sombra += '-'
    else:
        sombra += '_'
        qtd_letras += 1
sombra = f'{sombra:^{espacamento}}'
tentativas = 0; maximo_tentativas = 5 # <1 para terminar, se não tem uma tentativa a mais
banco = '  Banco de letras: '; banco = f'{banco:<{espacamento}}'

# TODO : fazer aceitar letras sem o acento

# while vencer or tentativas < maximo_tentativas :
#    letra = input('Insira uma letra: ')
#    if letra in forca :
#        print('ok')
#    else :
#        print(f'Não tem a letra {letra} na palavra.')
#        tentativas = tentativas + 1
#        print(f'Você tem mais {maximo_tentativas - tentativas} tentativas.')

##############################
# - feito na aula do curso - #
##############################

digitadas = []
textoinput = '  Digite uma letra: '; textoinput = f'{textoinput:{design}>{29}}'
while True:
    ######################################
    # - Estrutura Gráfica de Repetição - #
    ######################################
    quantidade = f'  A palavra tem {qtd_letras} letra(s).' 
    tent = f'Você tem {maximo_tentativas-tentativas} tentativa(s) restante(s).  '
    quantidade = f'{quantidade:<{52}}{tent}' # TODO :automatizar esta parte
    
    print(f'{design:{design}^{largura}}') 
    print(f'{espaco:{design}^{largura}}')
    print(f'{quantidade:{design}^{largura}}')
    print(f'{dica:{design}^{largura}}')
    print(f'{sombra:{design}^{largura}}')
    print(f'{espaco:{design}^{largura}}')
    print(f'{banco:{design}^{largura}}')
    print(f'{espaco:{design}^{largura}}')
    print(f'{design:{design}^{largura}}') 
    
    tentativas += 1
    l = input(textoinput)
    if l in forca:
        tentativas -= 1
        qtd = forca.count(l)
        linforca = f'  A palavra do jogo tem {qtd} letra(s) "{l}".  '
        linforca = f'{linforca:<{espacamento}}'
        print(f'{design:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
        print(f'{linforca:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
    else:
        lnotinforca = f'  A palavra do jogo não tem nenhuma letra "{l}".  '
        lnotinforca = f'{lnotinforca:<{espacamento}}'
        print(f'{design:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
        print(f'{lnotinforca:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
    
    sombra = ''
    
    digitadas.append(l)
    
    for a in forca:
        if a in digitadas:
            sombra += a
        else:
            sombra += '_'
#    print('Palavra secreta: ')        
#    print(sombra)
#    print(f'{banco:{design}^{largura}}')
    sombra = f'{sombra:^{espacamento}}'
    banco = '  Banco de letras: ' 
    # TODO : não permitir repetição de letras no banco de letras e posicioná-las na ordem alfabética
    # print(*lista,sep=' ')
    for l in digitadas:
        banco += l; banco += ', '
    banco = banco[:-1]; banco = banco[:-1] # Retira a vírgula e espaço na última letra
    banco = f'{banco:<{espacamento}}'
    
    if '_' in sombra:
        continue
    else:
        quantidade = f'  A palavra tem {qtd_letras} letra(s).' 
        tent = f'Você tem {maximo_tentativas-tentativas} tentativa(s) restante(s).  '
        quantidade = f'{quantidade:<{52}}{tent}'  # TODO :automatizar esta parte
    
        print(f'{design:{design}^{largura}}') 
        print(f'{espaco:{design}^{largura}}')
        print(f'{quantidade:{design}^{largura}}')
        print(f'{dica:{design}^{largura}}')
        print(f'{sombra:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
        print(f'{banco:{design}^{largura}}')
        print(f'{espaco:{design}^{largura}}')
        print(f'{design:{design}^{largura}}') 
        
        ganhou = f' - Parabéns, você Ganhou! - '
        # print(f'{design:{design}^{largura}}')
        print(f'{ganhou:{design}^{largura}}')
        print(f'{design:{design}^{largura}}')
        break
        
# TODO : fazer o usuário perder também    
