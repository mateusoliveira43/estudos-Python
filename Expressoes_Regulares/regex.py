# https://docs.python.org/3/library/re.html
# https://docs.python.org/3/howto/regex.html
import re

# findall, search, sub, compile

string = 'Este é um teste de expressões regulares.'
print(re.search(r'teste', string))
print(re.findall(r'teste', string))
print(re.sub(r'teste', 'abc', string))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('', string))

print()
string = 'ÁA.'
print(re.search(r'[A-Z]', string))
