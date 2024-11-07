import time
import csv
import json
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_functions as mf
from DataStructures.Tree import red_black_tree as rb
from datetime import datetime
#fecha_str = "2016-04-19 14:43:51"
#"Reto-G03/Data/Challenge-3/"
def fecha_segundos(fecha_str):


  fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
  segundos = int(fecha_obj.timestamp())
  return segundos
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"accidents":None,"fecha":None}
    catalog["accidents"] = lt.new_list()
    catalog["fecha"]=rb.new_map()
    
    return catalog

 
# Funciones para la carga de datos
def carga_by_años(arbol,dic):
    segundos=fecha_segundos(dic['Start_Time'])
    if rb.contains(arbol,segundos)==True:
        valor=rb.get(arbol,segundos)
        lt.add_last(valor,dic)
        rb.put(arbol,segundos,valor)
        
        
    else:
        k=lt.new_list()
        lt.add_last(k,dic)
        rb.put(arbol,segundos,k)
 
def load_data(catalog, filename):
    
    """
    Carga los datos del reto
    """
    
    movies = csv.DictReader(open(".\\Data\\"+filename, encoding='utf-8'))
    for elemento in movies:
         
        rta = {}
        rta['ID'] = elemento['ID']
        rta['Source'] =  elemento['Source']
        rta['Severity'] = elemento['Severity']
        rta['Start_Time'] = elemento['Start_Time']
        rta['End_Time'] = elemento['End_Time']
        rta['Start_Lat'] = elemento['Start_Lat']
        rta['Start_Lng'] = elemento['Start_Lng']
        rta['End_Lat'] = elemento['End_Lat']
        rta['End_Lng'] = elemento['End_Lng']
        rta['Distance(mi)'] = elemento['Distance(mi)']
        rta['Description'] = elemento['Description']
        rta['Street'] = elemento['Street']
        rta['City'] = elemento['City']
        rta['County'] = elemento['County']
        rta['State'] = elemento['State']
        rta['Temperature(F)'] = elemento['Temperature(F)']
        rta['Wind_Chill(F)'] = elemento['Wind_Chill(F)']
        rta['Humidity(%)'] = elemento['Humidity(%)']
        rta['Pressure(in)'] = elemento['Pressure(in)']
        rta['Visibility(mi)'] = elemento['Visibility(mi)']
        rta['Wind_Direction'] = elemento['Wind_Direction']
        rta['Wind_Speed(mph)'] = elemento['Wind_Speed(mph)']
        rta['Precipitation(in)'] = elemento['Precipitation(in)']
        rta['Weather_Condition'] = elemento['Weather_Condition']
        carga_by_años(catalog["fecha"],rta)
        lt.add_last(catalog["accidents"],rta)

    return catalog
   

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog,fecha_i,fecha_f):
    arbol=catalog["fecha"]
    inic=fecha_segundos(fecha_i)
    finic=fecha_segundos(fecha_f)
    ini=rb.ceiling(arbol,inic)
    print(ini)
    
    fini=rb.floor(arbol,finic)
    print(fini)
    lista=rb.values(arbol,ini,fini)
    print("Lista jeje")
    return lista
    #print(lista)
    print("Lista jeje")
    """"

    dic={}
    for i in range(0,lt.size(lista)):
        for j in range(0,lt.size(lista["elements"][i])):
            if lista["elements"][i]["elements"][j]["Severity"]>=3 and lista["elements"][i]["elements"][j]["Visibility(mi)"]<1 and fecha_segundos(lista["elements"][i]["elements"][j]["End_Time"])<=finic:
                if lista["elements"][i]["elements"][j]["Street"] not in dic:
                    k=lista["elements"][i]["elements"][j]["Street"]
                    dic[k]={}
    """""


 

def req_5(catalog,fecha_inicio, fecha_fin, condiciones_climaticas):
    """
    Retorna el resultado del requerimiento 5
    """
        
    inicio_seg = fecha_segundos(fecha_inicio + " 00:00:00")
    fin_seg = fecha_segundos(fecha_fin + " 23:59:59")

    inicio = rb.ceiling(catalog['fecha'], inicio_seg)
    fin = rb.floor(catalog['fecha'], fin_seg)
    if inicio is None or fin is None:
        print("No se encontraron accidentes en el rango de fechas especificado.")
        return None
    
    accidentes_en_rango = rb.values(catalog["fecha"], inicio, fin)
    
    franjas = {
        "Mañana": {"total": 0, "severidad_suma": 0, "condiciones": {}},
        "Tarde": {"total": 0, "severidad_suma": 0, "condiciones": {}},
        "Noche": {"total": 0, "severidad_suma": 0, "condiciones": {}},
        "Madrugada": {"total": 0, "severidad_suma": 0, "condiciones": {}}
    }
  
    for lista_accidentes in accidentes_en_rango['elements']:  
        for accidente in lista_accidentes['elements']:  
             
            if accidente['Severity'] == '3' or accidente['Severity'] == '4':
                if accidente['Weather_Condition'] in condiciones_climaticas:
                           
                    start_time = datetime.strptime(accidente['Start_Time'], "%Y-%m-%d %H:%M:%S")
                    franja = obtener_franja_horaria(start_time.hour)
                            

                            
                    franjas[franja]["total"] += 1
                    franjas[franja]["severidad_suma"] += int(accidente['Severity'])

                        
                    condicion = accidente['Weather_Condition'].lower()
                    if condicion in franjas[franja]["condiciones"]:
                        franjas[franja]["condiciones"][condicion] += 1
                    else:
                        franjas[franja]["condiciones"][condicion] = 1

    
    resultados = lt.new_list()
    for franja, datos in franjas.items():
        if datos["total"] > 0:
            promedio_severidad = datos["severidad_suma"] / datos["total"]

            
            condicion_predominante = max(datos["condiciones"], key=datos["condiciones"].get)

            lt.add_last(resultados, {
                "franja_horaria": franja,
                "total_accidentes": datos["total"],
                "promedio_severidad": promedio_severidad,
                "condicion_predominante": condicion_predominante
            })
    resultados_ordenados = lt.quick_sort(resultados,sort_crit)
    
    return resultados_ordenados

def obtener_franja_horaria(hora):
    """
    Clasifica la hora en la franja horaria correspondiente.
    """
    if 6 <= hora < 12:
        return "Mañana"
    elif 12 <= hora < 18:
        return "Tarde"
    elif 18 <= hora < 24:
        return "Noche"
    else:
        return "Madrugada"
    
def sort_crit(accidente1, accidente2):
    
    if accidente1['total_accidentes'] > accidente2['total_accidentes']:
        return -1  
    elif accidente1['total_accidentes'] < accidente2['total_accidentes']:
        return 1  
    
    
    if accidente1['promedio_severidad'] > accidente2['promedio_severidad']:
        return -1  
    elif accidente1['promedio_severidad'] < accidente2['promedio_severidad']:
        return 1  
    
    return 0  

def req_6(catalog,fecha_inicio, fecha_fin, humedad_minima, lista_condados):
    """
    Retorna el resultado del requerimiento 6
    """
    
    inicio_seg = fecha_segundos(fecha_inicio + " 00:00:00")
    fin_seg = fecha_segundos(fecha_fin + " 23:59:59")

    
    inicio = rb.ceiling(catalog['fecha'], inicio_seg)
    fin = rb.floor(catalog['fecha'], fin_seg)


    
    if inicio is None or fin is None:
        print("No se encontraron accidentes en el rango de fechas especificado.")
        return None

    
    estadisticas_por_condado = {}

    
    accidentes_en_rango = rb.values(catalog["fecha"], inicio, fin)
    print(accidentes_en_rango['elements'])


    
    for lista_accidentes in accidentes_en_rango['elements']:
        for accidente in lista_accidentes['elements']:
            
            if accidente['Severity'] == "3" or accidente['Severity'] == "4":
                if accidente['Humidity(%)'] != '' and accidente['Humidity(%)'] is not None:
                    humedad = float(accidente['Humidity(%)'])
                    condado = accidente['County']
                    
                
                    if humedad >= humedad_minima and condado in lista_condados:
                        print(f"Accidente {accidente['ID']} en {condado} cumple con los criterios.")
                        
            
                        if condado not in estadisticas_por_condado:
                                
                                estadisticas_por_condado[condado] = {
                                    "total_accidentes": 0,
                                    "temperatura_suma": 0,
                                    "humedad_suma": 0,
                                    "viento_suma": 0,
                                    "distancia_suma": 0,
                                    "accidente_mas_grave": None,
                                    "max_severidad": -1
                                }

                            
                        estadisticas_por_condado[condado]["total_accidentes"] += 1
                        if accidente['Temperature(F)'] != '' and accidente['Temperature(F)'] is not None:
                                estadisticas_por_condado[condado]["temperatura_suma"] += float(accidente['Temperature(F)'])
                        if accidente['Humidity(%)'] != '' and accidente['Humidity(%)'] is not None:
                                estadisticas_por_condado[condado]["humedad_suma"] += float(accidente['Humidity(%)'])
                        if accidente['Wind_Speed(mph)'] != '' and accidente['Wind_Speed(mph)'] is not None:
                                estadisticas_por_condado[condado]["viento_suma"] += float(accidente['Wind_Speed(mph)'])
                        if accidente['Distance(mi)'] != '' and accidente['Distance(mi)'] is not None:
                                estadisticas_por_condado[condado]["distancia_suma"] += float(accidente['Distance(mi)'])

                            
                        if int(accidente['Severity']) > estadisticas_por_condado[condado]["max_severidad"]:
                                estadisticas_por_condado[condado]["max_severidad"] = int(accidente['Severity'])
                                estadisticas_por_condado[condado]["accidente_mas_grave"] = {
                                    "ID": accidente['ID'],
                                    "Fecha": accidente['Start_Time'],
                                    "Temperatura": accidente['Temperature(F)'],
                                    "Humedad": accidente['Humidity(%)'],
                                    "Distancia": accidente['Distance(mi)'],
                                    "Descripción": accidente['Description']
                                }

    
    resultados = lt.new_list()
    for condado, datos in estadisticas_por_condado.items():
        if datos["total_accidentes"] > 0:
            
            promedio_temperatura = datos["temperatura_suma"] / datos["total_accidentes"]
            promedio_humedad = datos["humedad_suma"] / datos["total_accidentes"]
            promedio_viento = datos["viento_suma"] / datos["total_accidentes"]
            promedio_distancia = datos["distancia_suma"] / datos["total_accidentes"]

            
            lt.add_last(resultados, {
                "condado": condado,
                "total_accidentes": datos["total_accidentes"],
                "promedio_temperatura": promedio_temperatura,
                "promedio_humedad": promedio_humedad,
                "promedio_viento": promedio_viento,
                "promedio_distancia": promedio_distancia,
                "accidente_mas_grave": datos["accidente_mas_grave"]
            })

    
    resultados_ordenados = lt.quick_sort(resultados, sort_por_accidentes)
    return resultados_ordenados

def sort_por_accidentes(dato1, dato2):
    """
    Criterio de ordenación por número de accidentes graves en el condado.
    """
    if dato1['total_accidentes'] > dato2['total_accidentes']:
        return -1
    elif dato1['total_accidentes'] < dato2['total_accidentes']:
        return 1
    return 0
    


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
