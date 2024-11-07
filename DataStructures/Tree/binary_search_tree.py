#pytest -v -k "test_binary_search_tree"
#python -m pytest -v -k " test_binary_search_tree "
from DataStructures.List import array_list as lt
from . import bst_node as node
def new_map():
     
    my_bst = {'root': None,
            'type': 'BST'}

    return my_bst

def put(my_bst,key,value):
     
    my_bst['root'] = insert_node(my_bst['root'],key,value)
    
    return my_bst
    
    
def insert_node(root,key,value):
    
    if root is None:
        return node.new_node(key, value)
    

    if key < root['key']:
        root['left'] = insert_node(root['left'], key, value)  
    elif key > root['key']:
        root['right'] = insert_node(root['right'], key, value)  
    else:
        root['value'] = value  
    
    
    root['size'] = 1 + (root['left']['size'] if root['left'] else 0) + (root['right']['size'] if root['right'] else 0)
    return root    

def get(my_bst,key):
    
    node = get_node(my_bst['root'], key)
    if node is None:
        return None  
    return node['value']  
        
def get_node(root,key):
    
    if root is None:
        return None 
    if key == root['key']:
        return root  
    elif key < root['key']:
        return get_node(root['left'], key)  
    else:
        return get_node(root['right'], key)  

def remove(my_bst, key):
    my_bst['root'] = remove_node(my_bst['root'], key)
    return my_bst

def remove_node(root, key):
    if root is None:
        return None  

    
    if key < root['key']:
        root['left'] = remove_node(root['left'], key)
    elif key > root['key']:
        root['right'] = remove_node(root['right'], key)
    else:
        
        if root['left'] is None and root['right'] is None:
            return None
        
        
        if root['left'] is None:
            return root['right']
        if root['right'] is None:
            return root['left']
        
        
        successor = find_min(root['right'])
        
        root['key'] = successor['key']
        root['value'] = successor['value']
        
        root['right'] = remove_node(root['right'], successor['key'])

    
    root['size'] = 1 + (root['left']['size'] if root['left'] else 0) + (root['right']['size'] if root['right'] else 0)
    
    return root

def find_min(node):
    while node['left'] is not None:
        node = node['left']
    return node

def size(my_bst):
    return size_node(my_bst['root'])

def size_node(root):
    if root is None:
        return 0  
    return root['left']["size"]+root["right"]["size"]+1
def is_empty(my_bst):
    if my_bst['root']==None:  
        return True
    else:
        return False 
    

def contains(my_bst, key):
    return contains_node(my_bst['root'], key)

def contains_node(root, key):
    if root is None:
        return False  
    
    if key == root['key']:
        return True  
    elif key < root['key']:
        
        return contains_node(root['left'], key)
    else:
       
        return contains_node(root['right'], key)
def key_set(my_bst):
    lista = lt.new_list()  
    return key_set_in_order(my_bst['root'], lista)

def key_set_in_order(root, lista):
    if root is None: 
        return lista  

    
    key_set_in_order(root['left'], lista)   
    lt.add_last(lista, root['key'])         
    key_set_in_order(root['right'], lista)  
    return lista
def value_set(my_bst):
    lista = lt.new_list()  
    return value_set_in_order(my_bst['root'], lista)
def value_set_in_order(root, lista):
    if root is None:
        return lista  

    
    value_set_in_order(root['left'], lista)   
    lt.add_last(lista, root['value'])         
    value_set_in_order(root['right'], lista)  
    return lista
def find_min1(node):
    if node is None:
        return None
    while node['left'] is not None:
        node = node['left']
    return node["key"]
def min_key(my_bst):
    if "root" not in my_bst or my_bst["root"] is None:
        return None
    return find_min1(my_bst["root"])
def find_max1(node):
    if node is None:
        return None
    while node['right'] is not None:
        node = node['right']
    return node["key"]
def max_key(my_bst):
    if "root" not in my_bst or my_bst["root"] is None:
        return None
    return find_max1(my_bst["root"])
def delete_min(my_bst):
    k=min_key(my_bst)
    if k!=None:
       return remove(my_bst,k)
def delete_max(my_bst):
    k=max_key(my_bst)
    if k!=None:
       return remove(my_bst,k)
def find_floor(node, key):
    if node is None:
        return None
    if node['key'] == key:
        return node['key']
    if node['key'] > key:
        return find_floor(node['left'], key)

    
    floor_key_in_right_subtree = find_floor(node['right'], key)
    if floor_key_in_right_subtree is not None:
        return floor_key_in_right_subtree
    
    
    return node['key']

def floor(my_bst, key):
    
    if my_bst["root"] is None:
        return None
    
    
    if contains(my_bst, key):
        return key
    
    
    floor = find_floor(my_bst['root'], key)
    
    
    if floor is None or floor > key:
        return None
    
    
    return floor
def find_ceiling(node, key):
    if node is None:
        return None
    if node['key'] == key:
        return node['key']
    if node['key'] < key:
        
        return find_ceiling(node['right'], key)

    
    ceiling_key_in_left_subtree = find_ceiling(node['left'], key)
    if ceiling_key_in_left_subtree is not None:
        return ceiling_key_in_left_subtree
    
    
    return node['key']

def ceiling(my_bst, key):
    if my_bst["root"] is None:
        return None
    
    
    if contains(my_bst, key):
        return key
    
    
    ceiling = find_ceiling(my_bst['root'], key)
    
    
    if ceiling is None or ceiling < key:
        return None
    
    
    return ceiling

def select_key(root,key):
    
    if (root is not None):
            cont = size_tree(root['left'])
            if (cont > key):
                return select_key(root['left'], key)
            elif (cont < key):
                return select_key(root['right'], key-cont-1)
            else:
                return root

def size_tree(root):
    if (root is None):
            return 0
    else:
        return root['size']
    
def select(my_bst,key):
    node = select_key(my_bst['root'], key)
    if (node is not None):
        return node['key']
    return node

def rank_keys(root,key):
    
    if root is not None:
        if key < root['key']:
            return rank_keys(root['left'], key)
        elif key > root['key']:
            leftsize = size_tree(root['left'])
            rank = rank_keys(root['right'], key)
            total = 1 + leftsize + rank
            return total
        else:
            return size_tree(root['left'])
    return 0

def rank(my_bst,key):
    
    return rank_keys(my_bst['root'], key)

def height_tree(root):
    if (root is None):
            return -1
    else:
        return 1 + max(height_tree(root['left']),
                        height_tree(root['right']))
        

def height(my_bst):
    
    return height_tree(my_bst['root'])

def rank_keys(root,key):
    
    if root is not None:
        if key < root['key']:
            return rank_keys(root['left'], key)
        elif key > root['key']:
            leftsize = size_tree(root['left'])
            rank = rank_keys(root['right'], key)
            total = 1 + leftsize + rank
            return total
        else:
            return size_tree(root['left'])
    return 0

def rank(my_bst,key):
    
    return rank_keys(my_bst['root'], key)

def keys_range(root, key_initial, key_final, list_key):
    
    if root is not None:
            
        if key_initial < root['key']:
                keys_range(root['left'], key_initial, key_final, list_key)
        if key_initial <= root['key'] <= key_final:
                lt.add_last(list_key,root['key'])  
        if key_final > root['key']:
                keys_range(root['right'], key_initial, key_final, list_key)
    return list_key

def keys(my_bst, key_initial, key_final):
    
    list_key = lt.new_list()
    list_key = keys_range(my_bst['root'], key_initial, key_final, list_key)
                            
    return list_key

def values_range(root, key_lo, key_hi, list_values):
    if root is not None:
        
        values_range(root['left'], key_lo, key_hi, list_values)

        if key_lo <= root['key'] <= key_hi:
            lt.add_last(list_values, root['value'])
 
        values_range(root['right'], key_lo, key_hi, list_values)

    return list_values

def values(my_bst, key_initial, key_final):
    list_values = lt.new_list()
    list_values = values_range(my_bst['root'], key_initial, key_final, list_values)
    return list_values