#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json
from datetime import datetime


with open('dados.json', 'r') as file:
    dados = json.load(file)


faturamento_diario = {}
for dia in dados:
    data = datetime(year=2023, month=3, day=dia['dia'])
    faturamento_diario[data] = dia['valor']


menor_valor = min(faturamento_diario.values())
maior_valor = max(faturamento_diario.values())


soma = 0
contagem = 0
for data, valor in faturamento_diario.items():
    if data.weekday() < 5 and valor > 0:
        soma += valor
        contagem += 1
media = soma / contagem


acima_da_media = 0
for valor in faturamento_diario.values():
    if valor > media:
        acima_da_media += 1


print('Menor valor de faturamento diário:', menor_valor)
print('Maior valor de faturamento diário:', maior_valor)
print('Número de dias com faturamento acima da média:', acima_da_media)


# In[ ]:




