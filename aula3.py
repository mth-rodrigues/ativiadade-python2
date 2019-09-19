# class CuboMagico():

#     def __init__(self, cores, lados):
#         self.colors = cores
#         self.sides = lados 
#     def get_cores(self):
#         return self.colors
#     def get_lados(self):
#         return self.sides  
#     def set_cores(self, pigmentos):
#         self.colors = pigmentos      
#     def set_lados(self, lados):
#         self.sides = lados

# lista_de_cores = ['vermelho', 'azul', 'verde', 'amarelo', 'branco', 'laranja']

# porco = CuboMagico(lista_de_cores, 6)      


# class Animal():
#     def __init__(self, pelo, especie, olhos, patas):
#         self.pelo = pelo
#         self.especie = especie
#         self.olhos = olhos
#         self.patas = patas

#     def get_all(self):
#         print("Esse animal é um {}, tem {} olhos e tem {} patas." .format(self.especie, self.olhos, self.patas))  
# porco = Animal(True, "Suino", 2, 4)  

# porco.get_all()

class ReceitaGenerica():
    comestivel = True

    def __init__(self, ingredientes, modo_de_preparo, tempo_de_preparo):
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
        self.tempo_de_preparo = tempo_de_preparo

    def get_all(self):
        print("Verifique se você possui todos os {}, inicie o {} seguindo as orientações, prestando sempre atenção no {}." .format(self.ingredientes, self.modo_de_preparo, self.tempo_de_preparo))
receita = ReceitaGenerica("ingredientes", "modo de preparo", "tempo de preparo")  

# receita.get_all()

class ReceitaDoce(ReceitaGenerica):
    def __init__(self, nome, ingredientes, modo_de_preparo, tempo_de_preparo):
        self.nome = nome
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
        self.tempo_de_preparo = tempo_de_preparo

    def get_all(self):
        print("Receita de {}\n {}\n -1 lata de leite condensado\n -1 lata de suco de maracujá (medida pela lata de leite condensado)\n -1 lata de creme de leite sem soro\n {}\n Em um liquidificador, bata o creme de leite, o leite condensado e o suco concentrado de maracujá.\n {}\n Em uma tigela, despeje a mistura e leve à geladeira por, no mínimo, 4 horas." .format(self.nome, self.ingredientes, self.modo_de_preparo, self.tempo_de_preparo))

receitaDoce = ReceitaDoce("Mousse de Maracujá", "Ingredientes", "Modo de Preparo", "Tempo de Preparo")     

receitaDoce.get_all()