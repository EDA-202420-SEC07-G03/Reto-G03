from DataStructures.List import array_list as lt
from.import map_functions as mp
from.import map_entry as me
import random as rd
def cmp_function(a,b):
    if a==b:
        return 0
def new_map(num_keys, load_factor, prime=109345121):
 
    capacity = mp.next_prime(num_keys//load_factor)
    scale = rd.randint(1, prime-1)
    shift = rd.randint(0, prime-1)
    hash_table = {'prime': prime,
                 'capacity': capacity,
                 'scale': scale,
                 'shift': shift,
                 'table':lt.new_list(),
                 'current_factor': 0,
                 'limit_factor': load_factor,
                 'size': 0,
                 'type': 'PROBING'}
    for _ in range(capacity):
       entry = me.new_map_entry(None, None)
       lt.add_last(hash_table['table'], entry)
    return hash_table
 
def put(my_map, key, value):
    
     
    if my_map['size']+1  > my_map['capacity']*  my_map['limit_factor']:
       rehash(my_map) 

    index = mp.hash_value(my_map, key)  
    añadir = me.new_map_entry(key, value)

    
    for _ in range(my_map["capacity"]):
        entry = my_map['table']["elements"][index]

        if entry['key'] is None:
            
            my_map['table']["elements"][index] = añadir
            my_map['size'] += 1  
            return my_map
        
        elif entry['key'] == key:
            
            entry['value'] = value
            my_map['table']["elements"][index] = entry
            return my_map

        
        index = (index + 1) %my_map["capacity"]

    return my_map  

def contains(my_map, key):
    
    for i in range(len(my_map["table"]["elements"])):
        entry = my_map['table']["elements"][i]  
        
        if entry['key'] == key:
            return True

    
    return False
def get(my_map, key):
    for i in range(len(my_map["table"]["elements"])):
        entry = my_map['table']["elements"][i]  
        
        if entry['key'] == key:
            return entry["value"]
def size(my_map):
    return my_map["size"]
def remove(my_map, key):
    if my_map["size"]==0:
        return my_map

    for i in range(len(my_map["table"]["elements"])):
        entry = my_map['table']["elements"][i]  
        
        if entry['key'] == key:
            my_map['table']["elements"][i]['key']=None
            my_map['table']["elements"][i]['value']=None
            my_map['table']["size"]-=1
            my_map["size"]-=1
            return my_map
def is_empty(my_map):
    devol=True
    if my_map["size"]>0:
        devol=False
    return devol
def key_set(my_map):
    lista=lt.new_list()
    for i in range(len(my_map["table"]["elements"])):
        entry = my_map['table']["elements"][i]
        if entry!={'key': None, 'value': None}:
           lt.add_last(lista,entry["key"])
    return lista
def value_set(my_map):
    lista=lt.new_list()
    for i in range(len(my_map["table"]["elements"])):
        entry = my_map['table']["elements"][i]
        if entry!={'key': None, 'value': None}:
           lt.add_last(lista,entry["value"])
    return lista

def find_slot(my_map, key, hash_value):
    capacity = len(my_map["table"]["elements"])
    index = hash_value
    
    for _ in range(capacity):
        entry = my_map["table"]["elements"][index]

        if entry["key"] == key:
            return True, index  
        
        if entry["key"] is None:
            return False, index  
        
        index = (index + 1) % capacity  

    return False, -1  

def is_available(table, pos):
    
    
    if pos < 0 or pos >= len(table['elements']):
        return False
      

    else:
        entry = table['elements'][pos]

        
        is_empty = entry is None
        is_freed = isinstance(entry, dict) and entry.get('key') is None

        return is_empty or is_freed




def rehash(my_map):
    
    old_table = my_map['table']  
    new_capacity = mp.next_prime(my_map['capacity'] * 2)  

    
    my_map['table'] = lt.new_list()
    for _ in range(new_capacity):
        entry = me.new_map_entry(None, None)
        lt.add_last(my_map['table'], entry)

    
    my_map['size'] = 0  
    my_map['capacity'] = new_capacity  

    for index in range(len(old_table['elements'])):
     entry = old_table["elements"][index]
    
    
     if entry['key'] is not None:
        
        put(my_map, entry['key'], entry['value'])
    return my_map      

