from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

edson = Usuario('edson')
bel = Usuario('bel')

lance_edson = Lance(edson, 100)
lance_bel = Lance(bel, 160)

leilao = Leilao('Celular')
leilao.lances.append(lance_edson)
leilao.lances.append(lance_bel)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi de {avaliador.menor_lance}')
print(f'O maior lance foi de {avaliador.maior_lance}')
