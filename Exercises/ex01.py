"""
Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h,  

exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da

multa, cobrando R$5 por cada Km acima da velocidade permitida.

"""


velocidade_maxima = 80 # Velocidade máxima


def multa(velocidade: int) -> int | None: 

  
  if velocidade > velocidade_maxima:

    return (velocidade-velocidade_maxima)*5

  
  return None 


# Função acima calcula o valor da multa, e, se caso a velocidade passada no 
# argumento velocidade for menor que 80, a função retorna None.


velocidade_atual_and_multa = multa(int(input("Por favor, informe a velocidade do seu carro.\n: ")))

"""
Agora, faço duas ações na mesma variavel, onde ela pergunta no console a velocidade do carro
e juntamente já passa o valor como argumento na função multa().
E nisso, retorna a multa, caso for maior que 80, ou None se for menor.
"""

if velocidade_atual_and_multa is not None:

  print(f"Opa, opa.\nVocê ultrapassou a velocidade máxima permitida nesta rodovia, que é de 80KM/h.\n\nVocê vai precisar pagar a multa de {velocidade_atual_and_multa} reais.")

else:

  print("Ok, você está na velocidade permitida nesta rodovia, prossiga com cuidado.")
  exit(0)

