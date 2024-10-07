from heap import HeapMax

h = HeapMax()

h.arrive(("Snoke","Operación de máxima seguridad","10:00 AM",100), 3)
h.arrive(("Kylo Ren","Revisión de tropas","11:00 AM",50), 3)
h.arrive(("Capitán Phasma","Control de la seguridad interna","12:00 PM",50), 2)
h.arrive(("Capitán Phasma","Revisión del equipamiento","12:30 PM",30), 2)
h.arrive(("Capitán Phasma","Planificación de entrenamiento","1:00 PM",70), 2)
h.arrive(("Capitán Phasma","Supervisión de la base","1:30 PM",20), 2)
h.arrive(("General Hux","Revisión de las instalaciones","9:00 AM",40), 1)
h.arrive(("General de la base","Supervisión del mantenimiento","1:00 PM",30), 1)
h.arrive(("General Hux","Reunión con oficiales","3:00 PM",80), 1)
h.arrive(("General de la base","Inspección de las defensas","4:00 PM",70), 1)

agregar_operacion = input("¿Desea agregar otra operación? (s/n)?: ")

if agregar_operacion.lower() == 's':
    encargado = input("Ingrese el encargado: ")
    descripcion = input("Ingrese la descripción: ")
    hora = input("Ingrese la hora: ")
    
    stormtroopers = input("Ingrese la cantidad de stormtroopers (opcional): ")
    
    if stormtroopers:
        stormtroopers = int(stormtroopers)  
    else:
        stormtroopers = None  
    
    prioridad = int(input("Ingrese la prioridad (1 - General, 2 - Capitán Phasma, 3 - Snoke/Kylo Ren): "))
    
    if prioridad not in [1, 2, 3]:
        print("Prioridad inválida. Ingrese 1, 2 o 3.")
    else:
        operacion = (encargado, descripcion, hora, stormtroopers)
        h.arrive(operacion, prioridad)
        print("Operación agregada con éxito.")
else:
    print("No se agregó ninguna operación.")

# print(h.elements)

for _ in range(5):
    operacion_atendida = h.atention()
    print("Operación atendida:", operacion_atendida)


encargado = "Capitán Phasma"
descripcion = "Revisión de intrusos en el hangar B7"
hora = "09:00"
stormtroopers = 25
prioridad = 2
nueva_operacion = (encargado, descripcion, hora, stormtroopers)

h.arrive(nueva_operacion, prioridad)
print("Operación agregada:", nueva_operacion)

print()
print("Atendiendo la sexta operación:")
operacion_atendida = h.atention()
print("Operación atendida:", operacion_atendida)

encargado = "Snoke"
descripcion = "Destruir el planeta Takodana"
hora = "12:00"
stormtroopers = None  
prioridad = 3
nueva_operacion = (encargado, descripcion, hora, stormtroopers)

h.arrive(nueva_operacion, prioridad)
print("Operación agregada:", nueva_operacion)

while len(h.elements) > 0:
    print(h.atention())


