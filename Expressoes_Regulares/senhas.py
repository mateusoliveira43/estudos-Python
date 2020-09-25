from random import randint, choice, shuffle
import re


def zero_a_nove():
    return chr(randint(48, 57))


def a_a_z():
    return chr(randint(97, 122))


def A_a_Z():
    return chr(randint(65, 90))


def strange_chars():
    rand_range = [
        randint(32, 47),  # \u0020-\u002F [ -\/]
        randint(58, 64),  # \u003A-\u0040 [:-@]
        randint(91, 96),  # \u005B-\u0060 [[-`]
        randint(123, 126),  # \u007B-\u007E [{-~]
    ]

    # [\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]
    # [ -\/:-@[-`{-~]

    return chr(choice(rand_range))


def create_pass(
        length=12,
        upper=True,
        lower=True,
        numbers=True,
        chars=True
):
    password = []

    for i in range(length):
        if numbers:
            password.append(zero_a_nove())
        if lower:
            password.append(a_a_z())
        if upper:
            password.append(A_a_Z())
        if chars:
            password.append(strange_chars())

    password = password[:length]
    shuffle(password)
    return ''.join(password)


if __name__ == '__main__':

    print('VÁLIDAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=True,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=True
        ))
    print()

    print('SEM MINÚSCULAS E NÚMEROS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=True,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('SEM NÚMEROS CARACTERES E MINÚSCULAS')
    for i in range(5):
        print(create_pass(
            length=12,
            chars=False,
            upper=True,
            lower=False,
            numbers=False
        ))
    print()

    print('QUANTIDADE INVÁLIDA (6)')
    for i in range(5):
        print(create_pass(
            length=6,
        ))
    print()

regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$'
re.compile(regex)

texto = '''
IusU1P+?7a9`
95fn[OSA]2*f
b6F%Q0X8nm+*
m5f3VN_m5,P<
r8l;H|GK9d.2
​
PN73V4]1\*W{
8}|77T#2{OOR
7RZ^389_`A}G
ED3(R<*N2?70
7I15<IA6_<A*
​
R%T~.W[;DN~C
#L_TOZ{W?{`H
PG}H`EK}W%;#
FK^/JWO:[{\O
H>[ZX[H)A~L|
​
DDDTHEEHPYEP
VPAESCUSMXYQ
GVYYLJCLELBE
VDTXADAPGVCL
WQFUDXMXMFVN
​
Dh7_3h
lW4:o0
6Rm3_u
49[Agv
Gra]20
'''

print(re.findall(regex, texto, flags=re.M))
