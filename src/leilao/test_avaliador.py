from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador


class TestAvaliador(TestCase):
    def setUp(self):
        self.mark = Usuario('mark')
        self.lance_mark = Lance(self.mark, 100)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_leilao_quando_avalia_lances_em_ordem_crescente(self):
        clay = Usuario('clay')
        lance_clay = Lance(clay, 160)

        self.leilao.lances.append(self.lance_mark)
        self.leilao.lances.append(lance_clay)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 160

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_leilao_quando_avalia_lances_em_ordem_decrescente(self):
        clay = Usuario('clay')
        lance_clay = Lance(clay, 160)

        self.leilao.lances.append(lance_clay)
        self.leilao.lances.append(self.lance_mark)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 160

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_mesmo_valor_para_o_menor_e_o_maior_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        self.leilao.lances.append(self.lance_mark)
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        valor_esperado = 100

        self.assertEqual(valor_esperado, avaliador.menor_lance)
        self.assertEqual(valor_esperado, avaliador.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances(self):
        clay = Usuario('clay')
        lance_clay = Lance(clay, 160)

        robert = Usuario('robert')
        lance_robert = Lance(robert, 200)

        self.leilao.lances.append(lance_clay)
        self.leilao.lances.append(lance_robert)
        self.leilao.lances.append(self.lance_mark)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
