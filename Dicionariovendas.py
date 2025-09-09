vendas = [10, 15, 20, 5, 0, 8, 12, 25, 30, 18] 

total = sum(vendas)

mais_vendas = max(vendas)
dia_mais_vendas = vendas.index(mais_vendas) + 1

menos_vendas = min(vendas)
dia_menos_vendas = vendas.index(menos_vendas) + 1

media = total / len(vendas)

dias_acima_media = [i+1 for i, v in enumerate(vendas) if v > media]

analise_vendas = {
    "Total de Vendas no Mês": total,
    "Dia com Mais Vendas": {"Dia": dia_mais_vendas, "Vendas": mais_vendas},
    "Dia com Menos Vendas": {"Dia": dia_menos_vendas, "Vendas": menos_vendas},
    "Média de Vendas por Dia": round(media, 2),
    "Dias com Vendas Acima da Média": dias_acima_media
}

print(analise_vendas)
