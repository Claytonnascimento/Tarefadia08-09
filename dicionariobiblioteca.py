livros = [
    ["Dom Casmurro", "Ana", 5],
    ["1984", "Carlos", 12],
    ["O Hobbit", "Marina", 3],
    ["Senhor dos Anéis", "João", 15]
]

livros_mais_7_dias = [livro for livro in livros if livro[2] > 7]

livro_mais_tempo = max(livros, key=lambda x: x[2])

usuarios = [livro[1] for livro in livros]

media_dias = sum(livro[2] for livro in livros) / len(livros)

sistema_biblioteca = {
    "Livros Emprestados > 7 dias": livros_mais_7_dias,
    "Livro Emprestado Há Mais Tempo": {
        "Título": livro_mais_tempo[0],
        "Usuário": livro_mais_tempo[1],
        "Dias": livro_mais_tempo[2]
    },
    "Usuários com Livros Emprestados": usuarios,
    "Média de Dias de Empréstimo": round(media_dias, 2)
}

print(sistema_biblioteca)
