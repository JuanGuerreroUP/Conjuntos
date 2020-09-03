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
    A.update(B)
    return setToList(A)
def func_inter(A, B): #^
    salida = []
    for a in A:
        for b in B:
            if b == a:
                salida.append(b)
    return salida
def func_diff(A,B): #-
    aux = A[:]
    for a in A:
        for b in B:
            if b == a:
                aux.remove(a)
    return aux
def func_sim(A,B): #+
    salida = func_union(A,B)
    inter = func_inter(A,B)
    return func_diff(salida,inter)

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