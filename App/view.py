import sys
from App import logic as logic
from itertools import islice
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Tree import red_black_tree as rbt
import time

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
    print(catalog["fecha"]["root"]["size"])
    print(catalog["lat"]["root"]["size"])
    print(catalog["lon"]["root"]["size"])
    print(len(catalog["lzt"]))
    print(len(catalog["lut"]))
    print(len(catalog["lit"]))

    
     


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


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


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(sol):
    print(sol)
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(sol):
    print(sol)
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


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
            print_req_1(control)

        elif int(inputs) == 3:
            visibility_range_input = input('Ingrese el rango de visibilidad: ')
            state_list_input = input('Ingrese una lista de estados (por sus abreviaturas): ')
            visibility_range = tuple(map(float, visibility_range_input.split(',')))
            state_list = state_list_input.replace(" ", "").split(',')
            
            print_req_2(control, visibility_range, state_list)

        elif int(inputs) == 4:
            print_req_3(control)

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
