import random

#classe ou super classe pai
class personagem():

  #construtor
  def __init__(self,nome: str, classe: str, vida: int, ataque: int):
    self.nome: str = nome
    self.classe: str = classe
    self.vida: int = vida
    self.ataque: int = ataque

  def atacar (self, alvo):
    dano = random.randint(1, self.ataque)
    alvo.receber_dano(dano)
    print(f"{self.nome} atacou {alvo.nome} e causou {dano} de dano!")
    
  def receber_dano(self, dano: int):
    self.vida -= dano

  def esta_vivo(self):
    return self.vida > 0


class paladino(personagem):
  def __init__(self, nome):
    super().__init__(nome,"paladino", 100, 20)

class mago(personagem):
  def __init__(self, nome):
    super().__init__(nome,"mago", 80, 30)

class elfo(personagem):
  def __init__(self, nome):
    super().__init__(nome,"elfo", 90, 25)

class humano(personagem):
  def __init__(self, nome):
    super().__init__(nome,"humano", 110, 18)

class orc (personagem):
  def __init__(self, nome):
    super().__init__(nome,"orc", 150, 15)