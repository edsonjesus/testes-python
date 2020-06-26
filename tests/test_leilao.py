from unittest import TestCase

from src.leilao.dominio import Usuario, Lance, Leilao


class TestLeilao(TestCase):
    def setUp(self):
        self.mark = Usuario('mark', 100.0)
        self.lance_mark = Lance(self.mark, 100.0)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_leilao_quando_avalia_lances_em_ordem_crescente(self):
        clay = Usuario('clay', 160.0)
        lance_clay = Lance(clay, 160.0)

        self.leilao.propoe(self.lance_mark)
        self.leilao.propoe(lance_clay)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 160.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        clay = Usuario('clay', 160.0)
        lance_clay = Lance(clay, 160.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(lance_clay)
            self.leilao.propoe(self.lance_mark)

    def test_deve_retornar_o_mesmo_valor_para_o_menor_e_o_maior_lance_quando_o_leilao_tiver_apenas_um_lance(self):
        self.leilao.propoe(self.lance_mark)

        valor_esperado = 100.0

        self.assertEqual(valor_esperado, self.leilao.menor_lance)
        self.assertEqual(valor_esperado, self.leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_o_leilao_tiver_tres_lances_em_ordem_crescente(self):
        clay = Usuario('clay', 160.0)
        lance_clay = Lance(clay, 160.0)

        robert = Usuario('robert', 200.0)
        lance_robert = Lance(robert, 200.0)

        self.leilao.propoe(self.lance_mark)
        self.leilao.propoe(lance_clay)
        self.leilao.propoe(lance_robert)

        menor_valor_esperado = 100
        maior_valor_esperado = 200

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_mark)
        quantidade_de_lances = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        marcelo = Usuario('marcelo', 200.0)
        lance_marcelo = Lance(marcelo, 200.0)

        self.leilao.propoe(self.lance_mark)
        self.leilao.propoe(lance_marcelo)
        quantidade_de_lances = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_mark_200 = Lance(self.mark, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_mark)
            self.leilao.propoe(lance_mark_200)