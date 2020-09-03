import conjuntos

class Arbol:
    valor = None
    left = None
    right = None
    def __init__(self,valor = None):
        self.valor = valor
    def doMath(self, universo):
        if self.left != None:
            self.left.doMath(universo)
            if(self.right != None):
                self.right.doMath(universo)
                #operador = self.valor
                self.valor = operacion(self.left.valor, self.right.valor, self.valor, universo)
                #print(self.left.valor,operador,self.right.valor,self.valor)
entrada = "p((AuB)-(B^A))"
#entrada = '1+2+3+4+5'
entrada = entrada.replace(" ", "")
# u ^ x - + p
def operacion(A,B,operador, universo):
    if isinstance(A, str):
        if A not in universo.keys():
            raise  Exception(str("No existe ", A , " en tu universo"))
        else:
            A = universo[A]

    if isinstance(B, str):
        if B not in universo.keys():
            raise  Exception(str("No existe ", B , " en tu universo"))
        else:
            B = universo[B]
    if operador == 'u':
        return conjuntos.func_union(A,B)
    if operador == '^':
        return conjuntos.func_inter(A,B)
    if operador == 'x':
        return conjuntos.func_cart(A,B)
    if operador == '-':
        return conjuntos.func_diff(A,B)
    if operador == '+':
        return conjuntos.func_sim(A,B)
    if operador == 'p':
        return conjuntos.func_potencia(A)
#%%
#quitar
COUNT = [5]  
def print2DUtil(root, space) :  
    if (root == None) : 
        return
    space += COUNT[0] 
    print2DUtil(root.right, space)  
    print()  
    for i in range(COUNT[0], space): 
        print(end = " ")  
    print(root.valor)  
    print2DUtil(root.left, space)  
def print2D(root) : 
    print2DUtil(root, 0)  
#%%
def parentesisChunk(entrada, inicio = 0):
    cuenta = 0
    fin = 0
    tam = len(entrada)
    for j in range(inicio,tam):
        if entrada[j] == ')':
            cuenta -=1
            if cuenta == 0:
                fin = j
                break
        elif entrada[j] == '(':
            cuenta += 1
    fin +=1
    #print(i)
    inicio = fin
    return fin + 1

operadores = ['u', '^', 'x', '-', '+', 'p']
def makeTree(entrada):
    tam = len(entrada)
    i = 0
    head = Arbol()
    trueHead = head
    if(tam == 1):
        head.valor = entrada[i]
    else:
        while i < tam:
            #A+B+C
            if entrada[i] in operadores[:] :
                if(head.valor != None):
                    head.left = Arbol(head.valor)
                head.valor = entrada[i]
                if(head.valor == operadores[-1]):
                    head.right = Arbol(0)
                i += 1
            else:
                branch = Arbol()
                if entrada[i] == '(':
                    temp = i
                    i = parentesisChunk(entrada, i) -1
                    branch = makeTree(entrada[temp+1:i-1])
                else:
                    branch.valor = entrada[i]
                    i += 1
                if head.left == None:
                    head.left = branch
                else:
                    head.right = branch
                    head = head.right
    return trueHead

