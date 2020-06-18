from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def test_avalia(self):
        edson = Usuario('edson')
        bel = Usuario('bel')

        lance_edson = Lance(edson, 100)
        lance_bel = Lance(bel, 160)

        leilao = Leilao('Celular')
        leilao.lances.append(lance_edson)
        leilao.lances.append(lance_bel)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 160

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
