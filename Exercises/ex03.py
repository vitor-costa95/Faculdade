"""
Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre 
na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se 
ficou acima da média 7.0).
"""
import os, time

class CalcularMedia:
  
  def __init__(self, nota_minima: float, alunos_e_informacoes: dict):
    
    self.alunos = [x for x in alunos_e_informacoes.get("Alunos").keys()]
    self.notas = [y for y in alunos_e_informacoes.get("Alunos").values()]
    self.nota_minima = nota_minima
    
    
    """
    -> Representaçào
    dict = {
      "Alunos": {
        "aluno_name": [notas]
      }
    }
    """
  
  @property 
  def media_final(self):
    
    notas_somadas = [sum(k)//2 for k in self.notas]
    msg = ""
    apro = self.aproveitamento_final()
    
    for i in range(0,len(self.alunos)):
      
      msg += f"""
      ->  MEDIA ESCOLAR  <--
        {self.nota_minima}
          
      -> Aluno(a): {self.alunos[i]}
      -> Notas: {self.notas[i][0]}, {self.notas[i][1]}
      -> Média Final: {notas_somadas[i]}
      -> Status: {'Aprovado' if notas_somadas[i] >= self.nota_minima else 'Reprovado'}
      -> Aproveitamento (em %): {apro.get(self.alunos[i]).get("aproveitamento")}
      
      -> Considerações Finais <- 
      {apro.get(self.alunos[i]).get("considerations")}
      
      """
    
    return msg
  
  
  def aproveitamento_final(self):

    calcular_porcentagem = lambda nota: float((nota*100)/10)
    aproveitamento = {}
    
    for pos,i in enumerate(self.notas):
      
      porcentagem = calcular_porcentagem(sum(i)//2)
      status_final = ''
      nota_lk = self.nota_minima - (porcentagem//10)
      porcentagem_nota = float(((porcentagem//10)*100)/self.nota_minima)
      
      if porcentagem//10 >= self.nota_minima:
    
        if nota_lk < 0 and nota_lk in [-9, -8, -7, -6, -5, -4, -3]:
          status_final = "Aprovado com certa folga!"
        elif nota_lk in [-2, -1]:
          status_final = "Aprovado com méritos."
        elif nota_lk == 0:
          status_final = "Aprovado na medida"
      else:
        if nota_lk > 1 and nota_lk in [9,8,7,6,5,4,3]:
          status_final = "Reprovado com passagem garantida ao próximo ano."
        elif nota_lk in [2,1]:
          status_final = "Reprovado mas consegue recuperar."
      
      aproveitamento.update({self.alunos[pos]: {"aproveitamento": f"{porcentagem_nota}%", "considerations": status_final}})
    return aproveitamento
    
  
print("""
Olá professor(a), bem vindo ao calculador de notas e aproveitamento.

Siga as instruções abaixo, e informe corretamente o que for pedido, ok?
""")
time.sleep(3.5)
os.system("cls" if os.system == "nt" else "clear")
informacoes = {
  "Alunos": {}
}

quantidade_de_alunos = int(input("Por favor, professor(a), digite a quantidade\nde alunos que deseja verificar: "))
os.system("cls" if os.system == "nt" else "clear")
media = int(input("E qual é a media mínima que você deseja usar como referência (eg. 7,0): "))
os.system("cls" if os.system == "nt" else "clear")

print("Ok professor(a), agora informe os nomes e notas de cada aluno(a).\n")

checkup = ""
for i in range(0,quantidade_de_alunos):
  
  informacoes.update(
    {
      "Alunos": {
        input(
          f"-> Digite o nome do {i+1}º aluno(a): "
        ):
          [float(x) for x in input(
            "-> Agora digite suas duas notas, separe-as com uma vírgula.\n: "
          ).strip().split(",") if x != ","]
        
      }})

  finalizacao = CalcularMedia(nota_minima=media, alunos_e_informacoes=informacoes)
  checkup += finalizacao.media_final+"\n"

print(checkup)
