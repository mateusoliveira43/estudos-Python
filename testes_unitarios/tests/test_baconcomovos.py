"""
TDD - Test Driven Development

RED
1 -> Criar o teste e ver falhar

GREEN
2 -> Criar o código e ver o teste passar

REFACTOR
3 -> Melhorar meu código
"""
try:
    import sys
    import os

    sys.path.append(
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                '../src'
            )
        )
    )
except:
    raise

import unittest
from baconcomovos import bacon_com_ovos

# python3.8 -m unittest -v


class TestBaconComOvos(unittest.TestCase):
    def test_bacon_com_ovos_deve_levantar_assertion_error_se_nao_receber_int(self):
        with self.assertRaises(AssertionError):
            bacon_com_ovos('0')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'bacon com ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'passar fome'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )

    def test_bacon_com_ovos_deve_retornar_bacon_se_entrada_for_multiplo_somente_de_3(self):
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'bacon'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )

    def test_bacon_com_ovos_deve_retornar_ovos_se_entrada_for_multiplo_somente_de_5(self):
        entradas = (5, 10, 20, 25, 35)
        saida = 'ovos'

        for entrada in entradas:
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(
                    bacon_com_ovos(entrada),
                    saida,
                    msg=f'"{entrada}" não retornou "{saida}"',
                )


if __name__ == '__main__':
    unittest.main(verbosity=2)
