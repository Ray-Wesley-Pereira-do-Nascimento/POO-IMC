class Pessoas():
  def __init__(self, nome, altura, peso, data_nascimento):
    self.nome = nome
    self.altura = altura
    self.peso = peso
    self.data_nascimento = data_nascimento

  def __str__(self):
    return f'\n\nID:{id(self)}  \nNome:{self.nome} \nAltura:{self.altura} \nPeso:{self.peso} \nNascimento:{self.data_nascimento} '

  def imc(self):
    self.imc = peso / altura ** 2
    if self.imc < 18.5:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Baixo Peso')
    elif self.imc >= 18.5 and self.imc < 24.9:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Peso Normal')
    elif self.imc == 25:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Sobrepeso')
    elif self.imc > 25 and self.imc <= 29.9:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Sobrepeso - Estagio: Pré-obeso')
    elif self.imc > 25 and self.imc >= 30 and self.imc <= 34.9:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Sobrepeso - Estagio: Obeso I')
    elif self.imc > 25 and self.imc >= 35  and self.imc <= 39.9:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Sobrepeso - Estagio: Obeso II')
    elif self.imc > 25 and self.imc >= 40:
      print(f'IMC:{self.imc:.1f} \nFaixa de Peso: Sobrepeso - Estagio: Obeso III')



nome = input('Digite seu nome: ').strip()
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
nascimento = input('Digite sua data de nascimento no formato dd/mm/yyyy: ')

p = Pessoas(nome, altura, peso, nascimento)
print(p)
p.imc()
