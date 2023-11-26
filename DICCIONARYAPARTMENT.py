#CREAMOS NUESTRO DICCIONARIO  LLAMADO DEPARTAMENTOS 
import random


DEPARTAMENTOS = {"Amazonas":   'Leticia',
                 "Antioquia":  'Medellin',
                 "Arauca" : '   Arauca' ,
                 "Atlántico" : 'Barranquilla' ,
                 "Bogotá"  :   'Bogotá',
                 "Bolívar" :   'Cartagena' ,
                 "Boyacá"  : ' Tunja' ,
                 "Caldas" : 'Manizales' ,
                 "Caquetá" : 'Florencia' ,
                 "Casanare" : 'Yopal' ,
                 "Cauca" : 'Popayán' ,
                 "Cesar" : 'Valledupar' ,
                 "Chocó" : 'Quibdó' , 
                 "Córdoba" : 'Montería' , 
                 "Guainía" : 'Inírida' , 
                 "Guaviare" : 'San José del Guaviare' , 
                 "Huila" : 'Neiva' , 
                 "La Guajira" : 'Riohacha' ,
                 "Magdalena" : 'Santa Marta' ,
                 "Meta" : 'Villavicencio' ,
                 "Nariño" : 'Pasto' ,
                 "Norte de Santander" :'Cúcuta' ,
                 "Putumayo" : 'Mocoa' , 
                 "Quindío" : 'Armenia' ,
                 "Risaralda" : 'Pereira' ,
                 "San Andrés y Providencia" : 'San Andrés' ,
                 "Santander" : 'Bucaramanga' ,
                 "Sucre" :'Sincelejo' ,
                 "Tolima" : 'Ibagué' ,
                 "Valle del Cauca" : ' Cali' , 
                 "Vaupés" : 'Mitú' , 
                 "Vichada" :'Puerto Carreño',
}


# Obtén una lista de las claves del diccionario
claves = list(DEPARTAMENTOS.keys())


# SELECCIONA UNA CLAVES ALEATORIAS
clave_aleatoria = random.choice(claves)


# SELECCIONA  CAPITALES  IGUALES
valor_aleatorio = DEPARTAMENTOS[clave_aleatoria]

intentos = 3
    
while intentos > 0:
        RESPUESTA = input(f"SEÑ@R USUARIO DIGITA LA CAPITAL DE -->:  {clave_aleatoria}? ---> (Escribe 'salir' para terminar): ")
        
        if RESPUESTA.lower() == 'salir':
            print("GRACIAS POR TU INTERACTIVIDAD , HASTA LUEGO")
            break
        
        if RESPUESTA == valor_aleatorio:
            print("CORRECTO")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"Respuesta incorrecta. Te quedan {intentos} intentos.")
            else:
                print("Hasta luego. Sigue intentando en otra oportunidad.")