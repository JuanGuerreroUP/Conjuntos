#%%
def setToList(A):
    salida = []
    for i in A:
        salida.append(i)
    return salida
def ListToSet(A):
    salida = set()
    for i in A:
        salida.add(i)
    return salida

def func_union(A, B): #u
    A = ListToSet(A)
    B = ListToSet(B)
    return setToList(A.union(B))
def func_inter(A, B): #^
    A = ListToSet(A)
    B = ListToSet(B)
    return setToList(A.intersection(B))
def func_diff(A,B): #-
    A = ListToSet(A)
    B = ListToSet(B)
    return setToList(A.difference(B))
def func_sim(A,B): #+
    A = ListToSet(A)
    B = ListToSet(B)
    return setToList(A.symmetric_difference(B))

def func_cart(A,B): #x
    salida = []
    for a in A:
        for b in B:
            salida.append([a,b])
    return salida
def func_potencia(A): #Juan #p(A)
    salida = [[]]
    for a in A:
        salida.extend([b+[a] for b in salida])
    return salida