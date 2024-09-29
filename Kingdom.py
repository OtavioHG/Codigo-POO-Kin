class Personagem:
    def __init__(self, nome, forca, inteligencia, carisma):
        self.nome = nome
        self.forca = forca
        self.inteligencia = inteligencia
        self.carisma =carisma
    
    def atacar(self):
        return f"{self.nome} esta atacando com a força {self.forca}"
    
    def lider(self):
        return f"{self.nome} está liderando com carisma {self.carisma}"
    


class Comantante(Personagem):
    def __init__(self, nome, forca, inteligencia, carisma, contidade_de_soldados, estrategia):
        super().__init__(nome, forca, inteligencia, carisma)
        self.contidade_de_soldados = contidade_de_soldados
        self.estrategia = estrategia
        
    def planejar_estrategia(self):
        return f"{self.nome} esta planejando uma estrategia de nivel {self.estrategia}"
    
    def lidera_tropa(self):
        return f"O Comantante {self.nome} esta liderando sua tropa de {self.contidade_de_soldados} em uma estratégia de nivel {self.estrategia}."
    
class General(Personagem):
    def __init__(self, nome, forca, inteligencia, carisma, estrategia):
        super().__init__(nome, forca, inteligencia, carisma)
        self.estrategia = estrategia
    
    def planejar_batalha(self):
        return f"{self.nome} está planejando uma estratégia de nível {self.estrategia}."

    def liderar_exercito(self):
        return f"O General {self.nome} está liderando seu exército em uma estratégia de nível {self.estrategia}."
    

class Soldado(Personagem):
    def __init__(self, nome, forca, inteligencia, carisma, rank):
        super().__init__(nome, forca, inteligencia, carisma)
        self.rank = rank
    
    def seguir_ordem(self):
        return f"O soldado {self.nome}, de rank {self.rank}, está seguindo as ordens do general."

# Classe Batalha
class Batalha:
    def __init__(self, exercito_1, exercito_2):
        self.exercito_1 = exercito_1
        self.exercito_2 = exercito_2
    
    def iniciar(self):
        return f"A batalha entre {self.exercito_1.nome} e {self.exercito_2.nome} começou!"
    


import unittest

# Supondo que as classes estão definidas no mesmo arquivo ou foram importadas corretamente.

class TestKingdom(unittest.TestCase):
    
    def test_personagem(self):
        personagem = Personagem("Shin", 95, 70, 85)
        self.assertEqual(personagem.atacar(), "Shin esta atacando com a força 95")
        self.assertEqual(personagem.lider(), "Shin está liderando com carisma 85")
    
    def test_comandante(self):
        comandante = Comantante("Ten", 80, 90, 70, 500, 85)
        self.assertEqual(comandante.planejar_estrategia(), "Ten esta planejando uma estrategia de nivel 85")
        self.assertEqual(comandante.lidera_tropa(), "O Comantante Ten esta liderando sua tropa de 500 em uma estratégia de nivel 85.")
    
    def test_general(self):
        general = General("Ousen", 85, 95, 80, 90)
        self.assertEqual(general.planejar_batalha(), "Ousen está planejando uma estratégia de nível 90.")
        self.assertEqual(general.liderar_exercito(), "O General Ousen está liderando seu exército em uma estratégia de nível 90.")
    
    def test_soldado(self):
        soldado = Soldado("Kyoukai", 75, 60, 50, "sargento")
        self.assertEqual(soldado.seguir_ordem(), "O soldado Kyoukai, de rank sargento, está seguindo as ordens do general.")
    
    def test_batalha(self):
        general_1 = General("Shin", 95, 70, 85, 80)
        general_2 = General("Ousen", 85, 95, 80, 95)
        batalha = Batalha(general_1, general_2)
        self.assertEqual(batalha.iniciar(), "A batalha entre Shin e Ousen começou!")

# Executando os testes
if __name__ == "__main__":
    unittest.main()
