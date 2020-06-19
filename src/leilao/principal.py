from src.leilao.dominio import Usuario, Lance, Leilao, Avaliador

mark = Usuario('mark')
clay = Usuario('clay')

lance_mark = Lance(mark, 100)
lance_clay = Lance(clay, 160)

leilao = Leilao('Celular')
leilao.lances.append(lance_mark)
leilao.lances.append(lance_clay)

for lance in leilao.lances:
    print(f'O usuário {lance.usuario.nome} deu um lance de {lance.valor}')

avaliador = Avaliador()
avaliador.avalia(leilao)
print(f'O menor lance foi de {avaliador.menor_lance}')
print(f'O maior lance foi de {avaliador.maior_lance}')
