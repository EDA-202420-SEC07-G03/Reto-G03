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
    
    movies = csv.DictReader(open("Reto-G03/Data/Challenge-3/"+filename, encoding='utf-8'))
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
                        dic[k]={"city":lista["elements"][i]["elements"][j]["City"],"county":lista["elements"][i]["elements"][j]["County"],"state":lista["elements"][i]["elements"][j]["State"],"pelig":3,"total3":1,"total4":0,"visi":float(lista["elements"][i]["elements"][j]["Visibility(mi)"]),"start":lista["elements"][i]["elements"][j]["Start_Time"],"end":lista["elements"][i]["elements"][j]["End_Time"]} 
                    else:
                        dic[k]={"city":lista["elements"][i]["elements"][j]["City"],"county":lista["elements"][i]["elements"][j]["County"],"state":lista["elements"][i]["elements"][j]["State"],"pelig":4,"total3":0,"total4":1,"visi":float(lista["elements"][i]["elements"][j]["Visibility(mi)"]),"start":lista["elements"][i]["elements"][j]["Start_Time"],"end":lista["elements"][i]["elements"][j]["End_Time"]} 
                elif k in dic and dic[k]["city"]==lista["elements"][i]["elements"][j]["City"] and dic[k]["county"]==lista["elements"][i]["elements"][j]["County"]and dic[k]["state"]==lista["elements"][i]["elements"][j]["State"]:
                    if int(lista["elements"][i]["elements"][j]["Severity"])==3:
                        dic[k]["pelig"]+=3
                        dic[k]["total3"]+=1
                        dic[k]["visi"]+=float(lista["elements"][i]["elements"][j]["Visibility(mi)"])
                    else:
                        dic[k]["pelig"]+=4
                        dic[k]["total4"]+=1
                        dic[k]["visi"]+=float(lista["elements"][i]["elements"][j]["Visibility(mi)"])


    for i in dic:
        dic[i]["pelig"]=dic[i]["pelig"]/(dic[i]["total3"]+dic[i]["total4"])
        dic[i]["visi"]=dic[i]["visi"]/(dic[i]["total3"]+dic[i]["total4"])
    return dic

    


 

def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog,lami,lamax,lomi,lomax):
    arbol1=catalog["lat"]
    ini1=rb.ceiling(arbol1,float(lami))
    fini1=rb.floor(arbol1,float(lamax))
    lista1=rb.values(arbol1,ini1,fini1)
    arbol2=catalog["lon"]
    ini2=rb.ceiling(arbol2,float(lomi))
    fini2=rb.floor(arbol2,float(lomax))
    lista2=rb.values(arbol2,ini2,fini2)
    lista3=lt.new_list()
    ids_array1 = {element['ID'] for group in lista1['elements'] for element in group['elements']}
    ids_array2 = {element['ID'] for group in lista2['elements'] for element in group['elements']}
    common_ids = list(ids_array1.intersection(ids_array2))
    if len(common_ids)>0:
     for i in range(0,lt.size(lista1)):
        for j in range(0,lt.size(lista1["elements"][i])):
         if lista1["elements"][i]["elements"][j]["ID"] in common_ids:
            lt.add_last(lista3,lista1["elements"][i]["elements"][j])
    return lista3
    
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
