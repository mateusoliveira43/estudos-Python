# Tipos de Dados
## Dados Primitivos

### Strings - str

```python
str : string
```
Interpretado como texto, tudo aquilo entre aspas.

Para usar ' ou " dentro de aspas, use as aspas distintas para enclausurar ou use `\'`, `\"`.
Exemplo: 
```python
'Isso é uma "string" (str).'
"Isso é uma 'string' (str)."
"Isso é uma \"string\" (str)."
'Isso é uma \'string\' (str).'
```
`string[k]`: acessa o `k`-ésimo termo da string. 

Lembre que o índice percorre de 0 à `len(string)-1`. `[inicio:fim:passo]` padrão: inicio = 0, fim = `len(string)-1`, passo = 1. Também podemos usar contagem negativa: -1 como último caractere até `-len(string)` como primeiro caractere.
```python
string.startswith('texto') : valor booleano para primeiro elemento da string.

string.split('separador') : separa os elementos da string em uma lista.

\ : é chamado de carctere de escape.

\n : pula uma linha no console.

\t : dá um Tab na string mostrada.
```
	
### Número Inteiro - int
```python	
int : número inteiro, isto é, sem casa decimais (sem .)
```
### Ponto Flutuante - float
```python
float : ponto flutuante: número real, ou seja, com casa decimal (com .)
```
### Valor Booleano - bool
```python
bool : valor boolenao, retorna True ou False
```

## Dados Secundários
	
### Listas - list
```python
tido de dado: list , lista = [l1,l2,...,ln], li pode ser qualquer tipo de dado.
```
`lista[k]` acessa o `k`-ésimo termo de lista (0 à `len(lista)-1`).

Podemos usar o comando `lista[inicio:fim:passo]` (fatiamento).

Podemos usar `+` para juntar listas. Podemos usar também `lista.extend(lista)`, `lista.append(dado)`, `lista.insert(posicao,dado)`.

Para remover termos da lista, podemos usar `lista.pop(indice)`, `del(lista[inicio:fim:passo])`.

máximo e mínimo da lista (entre int e float): `max(lista)}` e `min(lista)`.

função `list()` cria uma lista.

`'separador'.join(lista)`: transforma uma lista em uma string.

`for inidice, objeto in enumerate(objeto)` : desempacotamento. 

`var1,va2,...,varn = lista` , de `n` elementos ou `var1,va2,...,vark,*lista2, varn = lista`, `lista2` é uma lista dos elementos restantes.

### não valor - None
```python
tipo de dado: None , não valor
```
### n-tuplas - tuple
```python
tido de dado: tuple , n-tupla : (t1,t2,...,tn)
```
Diferença de tuplas e listas: tuplas não podem ser editadas.

### Dicionários - dict
```python
Tipo de dado: dict
```
`dicionario = {'chave1': 'valor chave1','chave2': 'valor chave2',...}`

`dicionario['nova chave'] = 'valor nova chave'`

Para acessar uma chave do dicionário: `dicionario['nome da chave']` (não por índice como listas e tuplas)

olhar para os valores das chaves em vez das chaves: `dicionario.values()`. Também: `dicionario.keys()` (acessa as chaves) e `dicionario.items()` (acessa os elementos separados por vírgulas)
	
### Conjuntos - set
	
`conjunto = {elem1, elem2, ..., elemN}`

Conjuntos não tem elementos duplicados.

Lembre que as chaves `{,}` são usadas para dicionários. Logo, `conjunto = {}` é um dicionário vazio. Um conjunto vazio é: `conjunto = set()`.

Posso adicionar elementos a um conjunto com `.add()`: `conjunto.add(elem)` (um único por vez)

Posso remover elementos de um conjunto com `.discard()`: `conjunto.discard(elem)` (um único por vez)

Para adicionar mais elementos de uma vez com `.update()`: `conjunto.update([lista dos elem])`

`conjunto.clear()` : remove todos os elementos da lista

União: `A | B` ou `A.union(B)`

Intersecção: `A & B` ou `A.intersection(B)`

Diferença: `A - B` ou `A.difference(B)` (lembre que essa operação não é simétrica)

Diferença simétrica: `A ^ B` ou `A.symmetric_difference(B)`
	
### Classes
```python
class Nome:  # Por convenção, o nome tem a primeira letra maiúscula
	def __init__(self, parametros_iniciais):
		self.parametro_inicial = parametro_inicial

	def metodo(self, parâmetros):
		#função
	
	variavel = 'valor'
```
`self` dentro de funções para usar argumento sendo o próprio objeto

`objeto = NomeClasse(parâmetros iniciais)`

`objeto.metodo` ou `objeto.parametro_inicial` ou `objeto.variavel` (ou `NomeClasse.variavel`)
```python	
@classmethod
def por_ano_nascimento(cls, nome, ano_nascimento):
	idade = cls.ano_atual - ano_nascimento
	return cls(nome, idade)
```
```python
# Getter
@property
def preco(self):
	return self._preco # colocar o underline antes para não criar loops no código
```
```python
# setter
@preco.setter
def preco(self, valor):
	if isinstance(valor, str):
		valor = valor.replace('R\$', '')
		valor = float(valor.replace(',', '.'))
		self._preco = valor
```
Posso mudar uma variável de uma classe fora do seu escopo: `NomeClasse.variavel = 'novo valor'`. Isso mudará o valor da variável no resto do código

Se fizer isso numa instância: 
```python
instancia = NomeClasse()
instancia.variavel = 'novo valor'
```
Vai mudar só para aquela instância
	
#### Convenções

variável precedida de `_` : privada, não é recomendável alterá-la

variável precedida de `__` : muito privada, não se deve alterá-la
	
#### Hierarquia de classes
```python
class Classe1:
	métodos
	
class Classe2(Classe1):
	métodos
```
A classe Classe2 tem acesso a todos os métodos de Classe1, mas não vice versa.

Para usar métodos de classes superiores: `ClasseSuperior.método(parâmetros)` ou `super().método(parâmetros)`
```python
class Retangulo:
	def __init__(self, x, y):
		self.largura = x
		self.altura = y
	
	# Modificando operadores
	def __add__(self, other):
		largura = self.largura + other.largura
		altura = self.altura + other.altura
		return Retangulo(largura, altura)
```

Tabela de operadores e seus métodos
| Operador      | Método        | Operação  |
| ------------- |---------------| ----------|
| `+` | `__add__` | adição |
| `-` | `__sub__` | subtração |
| `*` | `__mul__` | multiplicação |
| `/` | `__div__` | divisão |
| `//` | `__floordiv__` | divisão inteira |
| `%` | `__mod__` | módulo |
| `**` | `__pow__` | potência |
| `+` | `__pos__` | positivo |
| `-` | `__neg__` | negativo |
| `<` | `__lt__` | menor que |
| `>` | `__gt__` | maior que |
| `<=` | `__le__` | menor ou igual a |
| `>=` | `__ge__` | maior ou igual a |
| `==` | `__eq__` | igual a |
| `!=` | `__ne__` | diferente de |
| `<<` | `__lshift__` | deslocamento para a equerda |
| `>>` | `__rshift__` | deslocamento para a direita |
| `&` | `__and__` | E bit-a-bit |
| <code>&#124;</code> | `__or__` | OU bit-a-bit |
| `^` | `__xor__` | Ou exclusivo bit-a-bit |
| `~` | `__inv__` | inversão |
	
Métodos mágicos: https://rszalski.github.io/magicmethods/

Gerenciamento de contexto
```python
class AbrirArquivo:
	def __init__(self, arquivo, modo, enconding='utf-8'):
		self.nome = arquivo
		# self.modo = modo
		print('Inicializando a Classe')
		print('Abrindo o arquivo.')
		self.arquivo = open(arquivo, modo, encoding=enconding)
	
	def __enter__(self):
		print('Entrando na Classe')
		print('Retornando o arquivo.')
		return self.arquivo
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		print('Saindo da Classe')
		print('Fechando o arquivo.')
		self.arquivo.close()
		# Tratando exceções
		# exc_type : tipo da exceção
		# exc_val : valor da exceção
		# exc_tb : traceback da exceção
		return True  # Não mostra as exceções na tela
```
```python
with AbrirArquivo('teste.txt', 'w+') as file:
	print(f'{"#"*30}\nEscrevendo no arquivo...')
	file.write('Título\n\n')
	file.write(f'Corpo do texto.\n')
	file.write(f'Corpo do texto.\n')
	file.write(f'Corpo do texto.\n')
	file.write(f'Corpo do texto.\n')
	print(f'Fim da escrita do arquivo.\n{"#"*30}')
```
```python
# Metaclasses: Criar comportamentos nas classes herdadas
class Meta(type):
	def __new__(mcs, name, bases, namespace):
		print(mcs)
		print(name)
		print(bases)
		print(namespace)
	
	if 'metodo' not in namespace:
		print(f'Não existe metodo (atributo ou método) em {name}.')
	else:
		if not callable(namespace['metodo']):
			print(f'metodo não é método em {name}.')
	
	return type.__new__(mcs, name, bases, namespace)  # Para criação da metaclasse
	
	
class Classe(metaclass=Meta):  # Para herdar da metaclasse
	def __init__(self, nome):
		self.nome = nome
	
	metodo = 'valor'
	# def metodo(self):
	#     pass
```
Dataclasses
```python
from dataclasses import dataclass, field, asdict, astuple
	
	
@dataclass(eq=False, repr=True, order=False, frozen=False, init=True)
class Pessoa:
	"""
	init = True (padrão): cria o inicializador (__init__) de forma compacta
	frozen = False (padrão): se True, não podemos mexer ou criar atributos da clase
	order = False (padrão): se True, deixa comparar objetos (classes) (Ex.: <)
	repr = True (padrão): mostra o que é o objeto (classe) mais bonitinho
	eq = True (padrão): classes com mesmos argumentos se tornam iguais
	"""
	nome: str
	sobrenome: str = field(repr=False)  # Não aparece na representação (print(Pessoa))
	
	def __post_init__(self):
		if not isinstance(self.nome, str):
			raise TypeError(f'Tipo de dado inválido. '
				f'{type(self.nome)} não é uma string {self}.')
	
	@property
	def nome_completo(self):
		return f'{self.nome} {self.sobrenome}'
	
	
p1 = Pessoa('Mateus', 'Oliveira')
print(p1.nome_completo)
print(p1)
print(asdict(p1), type(asdict(p1)), asdict(p1)['nome'])  # Transforma em dicionário
print(astuple(p1), type(astuple(p1)))  # Transforma em tupla
```
```python
from enum import Enum, auto
	
	
class Direcoes(Enum):
	direita = 0 # Direcoes.direita.name = 'direita', Direcoes.direita.value = 0
	esquerda = auto()
	cima = auto()
	baixo = auto()
	
	
	def movimentacao(direcao):
		if not isinstance(direcao, Direcoes):
			raise ValueError(f'Personagem não pode se movimentar para {direcao}.')
		return print(f'Personagem se movimentou para {direcao.name}.')
	
	
	movimentacao(Direcoes.esquerda)
	movimentacao(Direcoes.direita)
	movimentacao(Direcoes.cima)
	movimentacao(Direcoes.baixo)
```
Criando um iterador
```python
class Lista:
	def __init__(self):
		self.__items = []
		self.__index = 0
	
	def add(self, valor):
		return self.__items.append(valor)
	
	def __getitem__(self, index):
		return self.__items[index]
	
	def __setitem__(self, index, valor):
		self.__items[index] = valor
	
	def __iter__(self):
		return self
	
	def __next__(self):
		try:
			item = self.__items[self.__index]
			self.__index += 1
			return item
		except IndexError:
			raise StopIteration
	
	def __str__(self):
		return f'{self.__class__.__name__}: {self.__items}'
```
`__str__` para o usuário e `__repr__` para desenvolvedor.
	