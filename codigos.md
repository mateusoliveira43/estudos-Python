# Códigos
	
## Comentários
	
Caracteres precedidos do símbolo `#` (cerquilha, ou pound, em inglês), serão interpretados como comentários pelo Python, isto é, não afetam o código quando compilado (interpretado).

Blocos de comentário: (DOCSTRINGS)
```python
"""

"""
```
O que estiver depois de `"""` e antes de `"""` (ou `'''` e `'''`) será um comentário.

### Docstrings
`''' '''`, string multilinha

Usar `help(nome_do_modulo)` para imprimir informações ao usuário (ou de objetos dentro do módulo).
Também é válido `print(nome_do_modulo.objeto.__doc__)`

posso (e devo) documentar objetos dentro do módulo: funções, classes, ... (primeira linha após criá-las, com aspas triplas)

dentro da documentação

`:param x: descrição` - parâmetro `x` (descrições)

`:type x: descrição` - tipo do dado `x` (especificidades)

`:return: descrição` - o que o objeto retorna (descrições)

`:rtype: descrição` - tipo do dado que o objeto retorna (especificidades)

`:raises TipoError: descrição` - tipo de erro que pode ocorrer
	
## Listas To Do
	
`# TODO`
Marcar objetivos não finalizados no código. 
	
## Variáveis
	
`variável = definição`

Iniciar com letras. Podem conter números e `_`.

invertendo variáveis: `x,y = y,x`. Pode-se fazer com mais variáveis.
	
## Documentação
	
definindo os tipos de dados de objetos

`nome_objeto: tipo_do_objeto = valor_do_objeto`

posso usar dentro dos parâmetros de uma função

Também posso especificar o tipo de dado da saída da função
```python
def funcao(param: int = valor) -> int:
return 2
```
Quando precisar usar mais de um tipo de dado, usar Union
```python
from typing import Union

tipo_dado = Union[int, float]
x: tipo_dado = -12
```

https://docs.python.org/3/library/stdtypes.html

Para deixar o código bonito no console: https://pyformat.info/