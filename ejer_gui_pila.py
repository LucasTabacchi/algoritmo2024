from pila import Stack

stack_1 = Stack()
stack_aux = Stack()
stack_interseccion = Stack()

class personaje_star_wars():
    def __init__(self,name):
        self.name = name
    
    def get_name(self):
            return self.name
    
    def __str__(self):
        return(f'{self.name}')
    
    
list_epi_5 =[
personaje_star_wars('Luke Skywalker'),
personaje_star_wars('Princess Leia'),
personaje_star_wars('Chewbacca'),
personaje_star_wars('Han Solo'),
personaje_star_wars('Darth Vader'),
personaje_star_wars('Yoda'),
personaje_star_wars('Lando Calrissian'),
personaje_star_wars('C-3PO'),
personaje_star_wars('R2-D2'),
personaje_star_wars('Emperor Palpatine'),
personaje_star_wars('Boba Fett')
]

list_epi_7 = [
    personaje_star_wars('Rey'),
    personaje_star_wars('Finn'),
    personaje_star_wars('Han Solo'),
    personaje_star_wars('Kylo Ren'),
    personaje_star_wars('Princess Leia'),
    personaje_star_wars('Poe Dameron'),
    personaje_star_wars('BB-8'),
    personaje_star_wars('Chewbacca'),
    personaje_star_wars('Luke Skywalker'),
    personaje_star_wars('Supreme Leader Snoke'),
    personaje_star_wars('Maz Kanata'),
]

# Agrega los nombres a las pilas stack1 y stack2
for nombre in list_epi_5:
    stack_1.push(nombre)


while stack_1.size() > 0:
     personaje = stack_1.pop()
     for personaje_1 in list_epi_7:
         stack_aux.push(personaje_1)

     while stack_aux.size() > 0:
            if personaje.get_name() == stack_aux.pop().get_name():
                 stack_interseccion.push(personaje)


while stack_interseccion.size() > 0:
     print(stack_interseccion.pop())