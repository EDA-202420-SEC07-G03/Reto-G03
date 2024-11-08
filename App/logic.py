import time
import csv
import json
from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mp
from DataStructures.Map import map_functions as mf
from DataStructures.Tree import red_black_tree as rb
from DataStructures.Tree import binary_search_tree as bs
from datetime import datetime



#Funciones para medir los tiempos de ejecución

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

def fecha_segundos(fecha_str):


  fecha_obj = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
  segundos = int(fecha_obj.timestamp())
  return segundos
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {"accidents":None,"fecha":None,"lat":None,"lon":None,"lit":None,"lut":None,"lzt":None}
    catalog["accidents"] = lt.new_list()
    catalog["fecha"]=rb.new_map()
    catalog["lat"]=rb.new_map()
    catalog["lon"]=rb.new_map()
    catalog["lit"]=[]
    catalog["lut"]=[]
    catalog["lzt"]=[]


    
    return catalog

 
# Funciones para la carga de datos
def carga_by_años(arbol,dic,catalog):
    segundos=fecha_segundos(dic['Start_Time'])
    if rb.contains(arbol,segundos)==True:
        valor=rb.get(arbol,segundos)
        lt.add_last(valor,dic)
        rb.put(arbol,segundos,valor)
        catalog["lzt"].append(1)
        
        
    else:
        k=lt.new_list()
        lt.add_last(k,dic)
        rb.put(arbol,segundos,k)
def carga_by_lat(arbol,dic,catalog):
    lat=float(dic['Start_Lat'])
    if rb.contains(arbol,lat)==True:
        valor=rb.get(arbol,lat)
        lt.add_last(valor,dic)
        rb.put(arbol,lat,valor)
        catalog["lut"].append(1)
        
        
    else:
        k=lt.new_list()
        lt.add_last(k,dic)
        rb.put(arbol,lat,k)
def carga_by_lon(arbol,dic,catalog):
    lon=float(dic['Start_Lng'])
    if rb.contains(arbol,lon)==True:
        valor=rb.get(arbol,lon)
        lt.add_last(valor,dic)
        rb.put(arbol,lon,valor)
        catalog["lit"].append(1)
        
        
    else:
        k=lt.new_list()
        lt.add_last(k,dic)
        rb.put(arbol,lon,k)

def load_data(catalog, filename):
    
    """
    Carga los datos del reto
    """
    accidents = csv.DictReader(open(".\\Data\\Challenge-3\\"+filename, encoding='utf-8'))
    
    for elemento in accidents:
         
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
        carga_by_años(catalog["fecha"],rta,catalog)
        carga_by_lat(catalog["lat"],rta,catalog)
        carga_by_lon(catalog["lon"],rta,catalog)
        lt.add_last(catalog["accidents"],rta)

    return catalog


# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    info = None
    for accidente in catalog['accidents']:
        if accidente['ID'] == id:
            info = accidente
    return info


def req_1(catalog,fecha_inicia,fecha_final):
    """
    Retorna el resultado del requerimiento 1
    """
    inicial_segs =  fecha_segundos(fecha_inicia)
    final_segs = fecha_segundos(fecha_final)
    inicio = rb.ceiling(catalog['fecha'],inicial_segs)
    fin = rb.floor(catalog['fecha'],final_segs)
    
    if inicio is None or fin is None:
        print("No se encontraron accidentes en el rango de fechas especificado.")
        return None
    
    accidentes_en_rango = rb.values(catalog['fecha'],inicio,fin)
    
    lista_filtrada = lt.new_list()
    
    for lista_accidentes in accidentes_en_rango['elements']:
        for accidente in lista_accidentes['elements']:
        
            id_accidente = accidente['ID']
            fecha_hora_inicio = accidente['Start_Time']
            ciudad = accidente['City']
            estado = accidente['State']
            descripcion = accidente['Description'][:40] 
            
            inicio = datetime.strptime(accidente['Start_Time'], "%Y-%m-%d %H:%M:%S")
            final = datetime.strptime(accidente['End_Time'], "%Y-%m-%d %H:%M:%S")
            duracion_horas = (final - inicio).total_seconds() / 3600

            
            lt.add_last(lista_filtrada,{
                "ID": id_accidente,
                "Fecha y Hora de Inicio": fecha_hora_inicio,
                "Ciudad": ciudad,
                "Estado": estado,
                "Descripción": descripcion,
                "Duración en horas": duracion_horas
            })
            
    lista_ordenada = lt.merge_sort(lista_filtrada,sort_por_fecha_y_severidad)
    
    return lista_ordenada
            
            
            
    
def sort_por_fecha_y_severidad(accidente1, accidente2):
    
    fecha1 = datetime.strptime(accidente1['Fecha y Hora de Inicio'], "%Y-%m-%d %H:%M:%S")
    fecha2 = datetime.strptime(accidente2['Fecha y Hora de Inicio'], "%Y-%m-%d %H:%M:%S")

    if fecha1 > fecha2:
        return -1
    elif fecha1 < fecha2:
        return 1

    
    if int(accidente1.get('Severity', 0)) > int(accidente2.get('Severity', 0)):
        return -1
    elif int(accidente1.get('Severity', 0)) < int(accidente2.get('Severity', 0)):
        return 1

    return 0    


def req_2(catalog, visibility_range, state_list):
    """
    Retorna el resultado del requerimiento 2
    """
    resultados_estados = {}
    total_accidentes = 0
    
    for i in range(lt.size(catalog["accidents"])):
        accident = lt.get_element(catalog["accidents"], i)
        if 'Visibility(mi)' in accident:
            if 'Severity' in accident:
                if 'State' in accident:
                    if 'Distance(mi)' in accident:                        
                        visibility_str = accident['Visibility(mi)']
                        severity_str = accident['Severity']
                        state = accident['State']
                        distance_str = accident['Distance(mi)']
                        if visibility_str and severity_str and state and distance_str:
                            visibility = float(visibility_str)
                            severity = int(severity_str)
                            distance = float(distance_str)
                            if severity == 4:
                                if visibility_range[0] <= visibility <= visibility_range[1]:
                                    if state in state_list:
                                        total_accidentes += 1
                                        if state not in resultados_estados:
                                            resultados_estados[state] = {
                                                'count': 0,
                                                'total_visibility': 0,
                                                'total_distance': 0,
                                                'max_distance': None
                                            }
                                        state_data = resultados_estados[state]
                                        state_data['count'] += 1
                                        state_data['total_visibility'] += visibility
                                        state_data['total_distance'] += distance
                                        if (state_data['max_distance'] is None or 
                                            distance > float(state_data['max_distance']['Distance(mi)'])):
                                            state_data['max_distance'] = accident
    for state, data in resultados_estados.items():
        data['average_visibility'] = data['total_visibility'] / data['count']
        data['average_distance'] = data['total_distance'] / data['count']
        print(f"Estado: {state}, Promedio de visibilidad: {data['average_visibility']}, Promedio de distancia: {data['average_distance']}")
    sorted_states = sorted(resultados_estados.items(),key=lambda x: (-x[1]['count'], x[1]['average_visibility']))
    
    resultado = {
        'total_accidentes': total_accidentes,
        'state_analysis': sorted_states
    }

    return resultado




def req_3(catalog, n):
    """
    Retorna el resultado del requerimiento 3
    """
    n = int(n)
    accidentes_recientes = []

    for i in range(lt.size(catalog["accidents"])):
        accidente = lt.get_element(catalog["accidents"], i)
        visibility_str = accidente.get('Visibility(mi)', '')
        if visibility_str and accidente.get('Weather_Condition') and accidente['Severity'] in {'3', '4'}:
            if any(cond in accidente['Weather_Condition'].lower() for cond in ["rain", "snow"]):
                visibility = float(visibility_str) if visibility_str else float('inf')
                if visibility < 2:
                    accidentes_recientes.append(accidente)
    accidentes_recientes.sort(
        key=lambda x: (datetime.strptime(x['Start_Time'], "%Y-%m-%d %H:%M:%S"),-int(x['Severity'])), reverse=True
    )
    
    accidentes_recientes = accidentes_recientes[:n]
    visibilidad_total = sum(float(a['Visibility(mi)']) for a in accidentes_recientes if a.get('Visibility(mi)'))
    visibilidad_promedio = visibilidad_total / len(accidentes_recientes) if accidentes_recientes else 0

    resultado = {
        "average_visibility": visibilidad_promedio,
        "accidents": accidentes_recientes
    }

    return resultado



def req_4(catalog,fecha_i,fecha_f):
    arbol=catalog["fecha"]
    inic=fecha_segundos(fecha_i)
    finic=fecha_segundos(fecha_f)
    ini=rb.ceiling(arbol,inic)
    fini=rb.floor(arbol,finic)
    lista=rb.values(arbol,ini,fini)
    dic={}
    for i in range(0,lt.size(lista)):
        for j in range(0,lt.size(lista["elements"][i])):
           if lista["elements"][i]["elements"][j]["Visibility(mi)"]!='':
            if int(lista["elements"][i]["elements"][j]["Severity"])>=3 and float(lista["elements"][i]["elements"][j]["Visibility(mi)"])<1 and fecha_segundos(lista["elements"][i]["elements"][j]["End_Time"])<=finic:
                k=lista["elements"][i]["elements"][j]["Street"]
                if k not in dic:
                    if int(lista["elements"][i]["elements"][j]["Severity"])==3:
                        dic[k]={"city":lista["elements"][i]["elements"][j]["City"],"county":lista["elements"][i]["elements"][j]["County"],"state":lista["elements"][i]["elements"][j]["State"],"street":k,"pelig":3,"total3":1,"total4":0,"visi":float(lista["elements"][i]["elements"][j]["Visibility(mi)"]),"start":lista["elements"][i]["elements"][j]["Start_Time"],"end":lista["elements"][i]["elements"][j]["End_Time"]} 
                    else:
                        dic[k]={"city":lista["elements"][i]["elements"][j]["City"],"county":lista["elements"][i]["elements"][j]["County"],"state":lista["elements"][i]["elements"][j]["State"],"street":k,"pelig":4,"total3":0,"total4":1,"visi":float(lista["elements"][i]["elements"][j]["Visibility(mi)"]),"start":lista["elements"][i]["elements"][j]["Start_Time"],"end":lista["elements"][i]["elements"][j]["End_Time"]} 
                elif k in dic and dic[k]["city"]==lista["elements"][i]["elements"][j]["City"] and dic[k]["county"]==lista["elements"][i]["elements"][j]["County"]and dic[k]["state"]==lista["elements"][i]["elements"][j]["State"]:
                    dic[k]["visi"]+=float(lista["elements"][i]["elements"][j]["Visibility(mi)"])
                    if int(lista["elements"][i]["elements"][j]["Severity"])==3:
                        dic[k]["pelig"]+=3
                        dic[k]["total3"]+=1
                        
                    else:
                        dic[k]["pelig"]+=4
                        dic[k]["total4"]+=1
                        


    for i in dic:
        dic[i]["pelig"]=dic[i]["pelig"]/(dic[i]["total3"]+dic[i]["total4"])
        dic[i]["visi"]=dic[i]["visi"]/(dic[i]["total3"]+dic[i]["total4"])
    ordenado = dict(sorted(dic.items(), key=lambda item: (item[1]['state'], item[1]['county'], item[1]['city'], item[0])))
    return ordenado



def req_5(catalog,fecha_inicio,fecha_fin,condiciones_climaticas):
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



    
    for lista_accidentes in accidentes_en_rango['elements']:
        for accidente in lista_accidentes['elements']:
            
            if accidente['Severity'] == "3" or accidente['Severity'] == "4":
                if accidente['Humidity(%)'] != '' and accidente['Humidity(%)'] is not None:
                    humedad = float(accidente['Humidity(%)'])
                    condado = accidente['County']
                    
                
                    if humedad >= humedad_minima and condado in lista_condados:
                        
            
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
  
    if dato1['total_accidentes'] > dato2['total_accidentes']:
        return -1
    elif dato1['total_accidentes'] < dato2['total_accidentes']:
        return 1
    return 0


def req_7(catalog,lami,lamax,lomi,lomax):
    arbol1=catalog["lat"]
    ini1=rb.ceiling(arbol1,float(lami))
    fini1=bs.max_key(arbol1)
    lista1=rb.values(arbol1,ini1,fini1)
    arbol2=catalog["lon"]
    ini2=rb.ceiling(arbol2,float(lomi))
    fini2=bs.max_key(arbol2)
    lista2=rb.values(arbol2,ini2,fini2)
    lista3=lt.new_list()
    ids_array1 = {element['ID'] for group in lista1['elements'] for element in group['elements']}
    ids_array2 = {element['ID'] for group in lista2['elements'] for element in group['elements']}
    common_ids = list(ids_array1.intersection(ids_array2))
    total=0
    dic={}
    if len(common_ids)>0:
     for i in range(0,lt.size(lista1)):
        for j in range(0,lt.size(lista1["elements"][i])):
         if lista1["elements"][i]["elements"][j]["ID"] in common_ids:
            lt.add_last(lista3,lista1["elements"][i]["elements"][j])
    for i in range(0,lt.size(lista3)):
        if lista3["elements"][i]["End_Lat"]!=''and lista3["elements"][i]["End_Lng"]!='':
            if float(lami)<=float(lista3["elements"][i]["End_Lat"])<=float(lamax) and float(lomi)<=float(lista3["elements"][i]["End_Lng"])<=float(lomax) and float(lista3["elements"][i]["Start_Lat"])<=float(lamax) and float(lista3["elements"][i]["Start_Lng"])<=float(lomax):
                total +=1
                lista3["elements"][i]["duracion"]=(fecha_segundos(lista3["elements"][i]["End_Time"])/3600)-(fecha_segundos(lista3["elements"][i]["Start_Time"])/3600)
                dic[lista3["elements"][i]["ID"]]=lista3["elements"][i]
    sorted_data = dict(sorted(
    dic.items(), 
    key=lambda item: (
        float(item[1]['Start_Lat']), 
        float(item[1]['Start_Lng']), 
        float(item[1]['End_Lat']), 
        float(item[1]['End_Lng']))))
    return sorted_data,total





def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass

