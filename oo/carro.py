class Motor:
  def __init__(self) -> None:
    self.velocidade = 0

  def acelerar(self):
    self.velocidade += 1

  def frear(self):
    self.velocidade -= 2;
    self.velocidade = max(0, self.velocidade)

class Direcao:
  direcao = ['Norte', 'Leste', 'Sul', 'Oeste']
  
  def __init__(self) -> None:
    self.valor = Direcao.direcao[0]
  
  def girar_a_direita(self):
    self.valor =  Direcao.direcao[0] if self.valor == Direcao.direcao[-1] else Direcao.direcao[Direcao.direcao.index(self.valor)+1]
    
  def girar_a_esquerda(self):
    self.valor =  Direcao.direcao[-1] if self.valor ==  Direcao.direcao[0] else Direcao.direcao[Direcao.direcao.index(self.valor)-1]

    """
     N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    """

class Carro:
  def __init__(self, direcao = Direcao(), motor = Motor()) -> None:
    self.motor = motor
    self.direcao = direcao 
    
  def calcular_velocidade(self):
    return self.motor.velocidade
  
  def acelerar(self):
    self.motor.acelerar()
  
  def frear(self):
    self.motor.frear()
    
  def calcular_direcao(self):
    return self.direcao.valor
  
  def girar_a_direita(self):
    self.direcao.girar_a_direita()
  
  def girar_a_esquerda(self):
    self.direcao.girar_a_esquerda()
  
if __name__ == '__main__':
  carro = Carro()