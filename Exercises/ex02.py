"""
Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e
depois mostre se ela pode ou não votar.
"""
from datetime import date

# Variaveis
data_de_nascimento = [int(x) for x in input("[i] Digite sua data de nascimento, escreva assim: dd/mm/yy.\n: ").strip().split("/") if x != "/"]
dia, mes, ano = data_de_nascimento

aniversario_data = date(year = ano, day = dia, month = mes)
niver = abs(date.today() - aniversario_data).days // 365 
"""
Sobre os votos

No Brasil, entre 16-17 anos, o jovem já pode votar, mas não é algo obrigatório.

Já com 18 anos ou mais, torna-se obrigatório.
"""

idade_minima = 16
idade_obrigatoria = 18


if niver < idade_obrigatoria and niver >=idade_minima:
  print(f"Você possuí {niver} anos, e já está apto a votar, mas não é OBRIGATÓRIO.")
else:
  print(f"Você possuí {niver} anos, já é maior de idade, e com isso, é obrigatório votar.")
