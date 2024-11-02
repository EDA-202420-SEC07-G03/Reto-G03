#pytest -v -k "test_red_black_tree"
#python -m pytest -v -k " test_red_black_tree "
from . import rbt_node as node
from DataStructures.List import array_list as lt

#PRINCIPALES#


def new_map():
    my_rbt = {'root':None,
              'type': 'RBT'}
    
    return my_rbt

def put(my_rbt, key, value):
    
    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    my_rbt['root']['color'] = node.BLACK
    return my_rbt

def get(my_rbt, key):
    
    node = get_node(my_rbt['root'], key)
    return node['value'] if node is not None else None

def contains(my_rbt, key):
    
    if (my_rbt['root'] is None):
            return False
    else:
        return (get(my_rbt, key) is not None)
    
def size(my_rbt):
    
    return size_tree(my_rbt['root'])

def is_empty(my_rbt):
    
    return (my_rbt['root'] is None)

def key_set(my_rbt):
    
    lista = lt.new_list()  
    return key_set_tree(my_rbt['root'], lista)

def value_set(my_rbt):
    lista = lt.new_list()  
    return value_set_tree(my_rbt['root'], lista)

def min_key(my_rbt):
    
    
    if my_rbt is None or my_rbt['root'] is None:
        return None
   
    return min_key_tree(my_rbt['root'])['key']


def max_key(my_rbt):
    
    if my_rbt is None or my_rbt['root'] is None:
        return None
    return max_key_tree(my_rbt['root'])['key']

def floor(my_rbt, key):
    
    node = floor_key(my_rbt['root'], key)
    if (node is not None):
        return node['key']
    return node  

def ceiling(my_rbt, key):
    
    node = ceiling_key(my_rbt['root'], key)
    if (node is not None):
        return node['key']
    return node


def select(my_rbt,key):
    node = select_key(my_rbt['root'], key)
    if (node is not None):
        return node['key']
    return node

def rank(my_rbt,key):
    
    return rank_keys(my_rbt['root'], key)


def height(my_rbt):
    
    return height_tree(my_rbt['root'])


def keys(my_rbt, key_initial, key_final):
    
    list_key = lt.new_list()
    list_key = keys_range(my_rbt['root'], key_initial, key_final, list_key)
                            
    return list_key


def values(my_rbt, key_initial, key_final):
    list_values = lt.new_list()
    list_values = values_range(my_rbt['root'], key_initial, key_final, list_values)
    return list_values

       
    
    
#AUXILIARES#
    

def insert_node(root,key,value):
    
    if root is None:     
        root = node.new_node(key, value, node.RED)
        return root

    
    if key < root['key']:     
        root['left'] = insert_node(root['left'], key, value)
    elif key > root['key']:   
        root['right'] = insert_node(root['right'], key, value)
    else:              
        root['value'] = value

    
    if is_red(root['right']) and not is_red(root['left']):
        root = rotate_left(root)
    if is_red(root['left']) and is_red(root['left']['left']):
        root = rotate_right(root)
    if is_red(root['left']) and is_red(root['right']):
        flip_colors(root)

    root['size'] = size_tree(root['left']) + size_tree(root['right']) + 1

    return root

def is_red(node_rbt):
    
    if (node_rbt is None):
            return False
    else:
        return (node_rbt['color'] == node.RED)
    
    
def rotate_left(rbt_node):
    x = rbt_node['right']
    rbt_node['right'] = x['left']
    x['left'] = rbt_node
    x['color'] = x['left']['color']
    x['left']['color'] = node.RED
    x['size'] = rbt_node['size']
    rbt_node['size'] = size_tree(rbt_node['left']) + size_tree(rbt_node['right']) + 1
    return x

def rotate_right(rbt_node):
    
    x = rbt_node['left']
    rbt_node['left'] = x['right']
    x['right'] = rbt_node
    x['color'] = x['right']['color']
    x['right']['color'] = node.RED
    x['size'] = rbt_node['size']
    rbt_node['size'] = size_tree(rbt_node['left']) + size_tree(rbt_node['right']) + 1
    return x

def size_tree(root):
    
    if (root is None):
            return 0
    else:
        return root['size']
    
def flip_colors(node_rbt):
    
    flip_node_color(node_rbt)
    flip_node_color(node_rbt['left'])
    flip_node_color(node_rbt['right'])
    
def flip_node_color(node_rbt):
    
    if (node_rbt is not None):
        if (node_rbt['color'] == node.RED):
            node_rbt['color'] = node.BLACK
        else:
            node_rbt['color'] = node.RED
            
def get_node(root, key):
    
    element = None
    if root is not None:
        
        if key < root['key']:
            element = get_node(root['left'], key)
        elif key > root['key']:
            element = get_node(root['right'], key)
        else:
            element = root
    return element

def key_set_tree(root, lista):
    if root is None:
        return lista  

    key_set_tree(root['left'], lista)   
    lt.add_last(lista, root['key'])         
    key_set_tree(root['right'], lista)  
    return lista


def value_set_tree(root, lista):
    if root is None:
        return lista  

    
    value_set_tree(root['left'], lista)   
    lt.add_last(lista, root['value'])         
    value_set_tree(root['right'], lista)  
    return lista

def min_key_tree(root):
    min = None
    if (root is not None):
        if (root['left'] is None):
            min = root
        else:
            min = min_key_tree(root['left'])
    return min


def max_key_tree(root):
    
    max = None
    if (root is not None):
        if (root['right'] is None):
                max = root
        else:
                max = max_key_tree(root['right'])
    return max


def floor_key(root, key):

    if root is not None:
        if key == root['key']:
            return root
        elif key < root['key']:
            return floor_key(root['left'], key)
        
        t = floor_key(root['right'], key)
        return t if t is not None else root
    return None


def ceiling_key(root, key):
    
    if root is not None:
        if key == root['key']:
            return root
        elif key < root['key']:
            t = ceiling_key(root['left'], key)
            return t if t is not None else root
        return ceiling_key(root['right'], key)
    return None


def select_key(root,key):
    
    if (root is not None):
            cont = size_tree(root['left'])
            if (cont > key):
                return select_key(root['left'], key)
            elif (cont < key):
                return select_key(root['right'], key-cont-1)
            else:
                return root
            

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


def height_tree(root):
    if (root is None):
            return -1
    else:
        return 1 + max(height_tree(root['left']),
                        height_tree(root['right']))   
        
        
def keys_range(root, key_initial, key_final, list_key):
    
    if root is not None:
            
        if key_initial < root['key']:
                keys_range(root['left'], key_initial, key_final, list_key)
        if key_initial <= root['key'] <= key_final:
                lt.add_last(list_key,root['key'])  
        if key_final > root['key']:
                keys_range(root['right'], key_initial, key_final, list_key)
    return list_key         


def values_range(root, key_lo, key_hi, list_values):
    if root is not None:
        
        values_range(root['left'], key_lo, key_hi, list_values)

        if key_lo <= root['key'] <= key_hi:
            lt.add_last(list_values, root['value'])
 
        values_range(root['right'], key_lo, key_hi, list_values)

    return list_values  






















    
    


    
    







    







        













