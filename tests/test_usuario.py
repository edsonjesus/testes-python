import pytest
from src.leilao.dominio import Usuario, Leilao


@pytest.fixture
def ronaldo():
    return Usuario('Ronaldo', 150.0)


@pytest.fixture
def leilao():
    return Leilao('Tablet')


def test_deve_subtrair_valor_da_carteira_do_usuario_quando_esse_propor_um_lance(ronaldo, leilao):
    ronaldo.propoe_lance(leilao, 100.0)
    assert ronaldo.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_do_que_o_valor_da_carteira(ronaldo, leilao):
    ronaldo.propoe_lance(leilao, 10.0)
    assert ronaldo.carteira == 140.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(ronaldo, leilao):
    ronaldo.propoe_lance(leilao, 150.0)
    assert ronaldo.carteira == 0.0


def test_nao_deve_permitir_propor_um_lance_maior_do_que_o_valor_que_o_usuario_tem_na_carteira(ronaldo, leilao):
    with pytest.raises(ValueError):
        ronaldo.propoe_lance(leilao, 200.0)
