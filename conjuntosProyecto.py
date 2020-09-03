#%%
import conjuntos
import textHandler
#%%
#tests
A = [1,2]
B = ['a','b']
B = conjuntos.func_potencia(B)
conjuntos.func_cart(A,B)

#%%
#User
nConjuntos = 0
universo = {}
while True:
    print ("Ingresa los elementos del conjunto ", chr(nConjuntos+65), ": (<ENTER> para terminar)") #mejor separados por comma, solo preguntar nombre del conjunto
    temp = set()
    valor = input()
    temp.update(valor.split(','))
    if(len(valor) == 0):
        break
    universo[chr(nConjuntos+65)] = conjuntos.setToList(temp)
    nConjuntos += 1
operadoresNom = ['unión', 'intersección','producto cartesiano', 'diferencia', 'diferencia simetrica', 'conjunto potencia']
print ("Simbología")
for i in range(len(operadoresNom)):
    print(textHandler.operadores[i],": ",operadoresNom[i])
while True:
    #operadores = ['u', '^', 'x', '-', '+', 'p']
    print ("Ingresa una operación con conjutos: ")
    operacion = input() # u(A,B)
    if(len(operacion) == 0):
        break
    operacion = operacion.replace(" ", "")
    try:
        head = textHandler.makeTree(operacion)
        head.doMath(universo)
        print(head.valor)
    except:
        print("Sintaxis incorrecta en la operación: ",operacion)

# %%
