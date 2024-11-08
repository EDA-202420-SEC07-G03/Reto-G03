import sys
from App import logic as logic
from itertools import islice
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Tree import red_black_tree as rbt
import time

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    filename = input("Ingrese el nombre del archivo (con el .csv): ")
    catalog = logic.load_data(control,filename)
    print('se han cargado ' + str(catalog['accidents']['size']) + " accidentes.")
    print('Los primeros 5 accidentes cargados son: ')
    print(catalog['accidents']['elements'][:5])
    print('Los últimos 5 accidentes cargados son: ')
    print(catalog['accidents']['elements'][-5:])

    
     


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id = input("Ingrese el ID del accidente que desea buscar: ")
    rta = logic.get_data(control,id)
    print(rta)

def print_req_1(control,fecha_inicio,fecha_fin):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """

    rta = logic.req_1(control,fecha_inicio,fecha_fin)
    print('Para el intervalo de fechas dado hay ' + str(rta['size']) + " accidentes")
    if rta['size'] > 10:
        print("Los primeros 5 accidentes son: ")
        print(rta['elements'][:6])
        print('Los últimos 5 accidentes son: ')
        print(rta['elements'][-5:])
    else:
        print(rta)
    


def print_req_2(control, visibility_range, state_list):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    resultado = logic.req_2(control, visibility_range, state_list)

    print("Total de accidentes que cumplen los criterios de visibilidad y gravedad:", resultado['total_accidentes'])

    print("Análisis por estado:")
    for state, data in resultado['state_analysis']:
        print(f"Estado: {state}")
        print(f"  - Número de accidentes: {data['count']}")
        print(f"  - Promedio de visibilidad: {data['average_visibility']:.2f} millas")
        print(f"  - Distancia promedio afectada: {data['average_distance']:.2f} millas")

        max_accident = data['max_distance']
        if max_accident:
            print("  - Accidente con mayor distancia afectada:")
            print(f"      ID: {max_accident['ID']}")
            print(f"      Fecha de inicio: {max_accident['Start_Time']}")
            print(f"      Visibilidad: {max_accident['Visibility(mi)']} millas")
            print(f"      Distancia afectada: {max_accident['Distance(mi)']} millas")
        else:
            print("  - No se encontraron accidentes con distancia afectada para este estado.")


def print_req_3(control, n):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    
    resultado = logic.req_3(control, n)
    
    print("La visibilidad promedio de los accidentes que cumplen con los criterios:", f"{resultado['average_visibility']:.2f} millas")

    print("Listado de accidentes:")
    for accidente in resultado['accidents']:
        print(f"  - ID del accidente: {accidente['ID']}")
        print(f"    Fecha y hora de inicio del accidente: {accidente['Start_Time']}")
        print(f"    Ciudad y Estado: {accidente['City']}, {accidente['State']}")
        print(f"    Condición de precipitación reportada: {accidente['Weather_Condition']}")
        print(f"    Severidad: {accidente['Severity']}")
        print(f"    Descripción del accidente: {accidente['Description'][:40]}")
        
        fecha_inicio = logic.datetime.strptime(accidente['Start_Time'], "%Y-%m-%d %H:%M:%S")
        fecha_fin = logic.datetime.strptime(accidente['End_Time'], "%Y-%m-%d %H:%M:%S")
        duracion = (fecha_fin - fecha_inicio).total_seconds() / 3600
        
        print(f"    Duración del accidente: {duracion:.2f} horas")


def print_req_4(sol):
    print(sol)


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    fecha_inicio = input("Ingrese la fecha de inicio: ")
    fecha_fin = input("Ingrese la fecha final: ")
    condiciones_climaticas = input("Ingrese las condiciones climaticas: ").split()
    rta = logic.req_5(control, fecha_inicio,fecha_fin,condiciones_climaticas)
    print(rta)


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    fecha_inicio = input("Ingrese la fecha de inicio: ")
    fecha_fin = input("Ingrese la fecha final: ")
    humedad = float(input("Ingrese la humedad mínima: "))
    condados = input("Ingrese los condados a consultar: ").split()
    rta = logic.req_6(control, fecha_inicio,fecha_fin,humedad,condados)
    print(rta)


def print_req_7(sol):
    if len(sol[0])>10:
     claves = list(sol[0].keys())
     print("Primeros 5 elementos:")
     for clave in claves[:5]:
       print(clave, ":", sol[0][clave])
     print("\nÚltimos 5 elementos:")
     for clave in claves[-5:]:
      print(clave, ":", sol[0][clave])
    else:
        print(sol[0])
    print("El total de elementos es " + str(sol[1]))
 
    

    
 

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 2:
            fecha_inicio = input("Ingrese la fecha de inicio (Formato %Y-%m-%d %H:%M:%S): ")
            fecha_fin = input("Ingrese la fecha final (Formato %Y-%m-%d %H:%M:%S): ")
            print_req_1(control, fecha_inicio, fecha_fin)
        

        elif int(inputs) == 3:
            visibility_range_input = input('Ingrese el rango de visibilidad: ')
            state_list_input = input('Ingrese una lista de estados (por sus abreviaturas): ')
            visibility_range = tuple(map(float, visibility_range_input.split(',')))
            state_list = state_list_input.replace(" ", "").split(',')
            
            print_req_2(control, visibility_range, state_list)

        elif int(inputs) == 4:
            n = input('Ingrese la cantidad de accidentes que quiere ver: ')
            
            print_req_3(control,n)

        elif int(inputs) == 5:
            ini = input('Ingrese la fecha inicial del periodo a consultar (en formato YYYY-MM-DD): ')
            fini = input('Ingrese la fecha final del periodo a consultar (en formato YYYY-MM-DD): ')
            sol=logic.req_4(control,ini,fini)
            print_req_4(sol)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            lami = input('Ingrese la latitud minima: ')
            lamax = input('Ingrese la latitud maxima: ')
            lomi = input('Ingrese la longitud minima: ')
            lomax = input('Ingrese la longitud maxima: ')
            sol=logic.req_7(control,lami,lamax,lomi,lomax)
            print_req_7(sol)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
