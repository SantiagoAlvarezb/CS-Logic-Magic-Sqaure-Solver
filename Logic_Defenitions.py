from random import choice
##############################################################################
# Variables globales
##############################################################################

# Crea las letras minúsculas a-z
letrasProposicionales = [chr(x) for x in range(256, 289)]
#print(letrasProposicionales)
# inicializa la lista de interpretaciones
listaInterpsVerdaderas = []
# inicializa la lista de hojas
listaHojas = []

##############################################################################
# Definición de objeto tree y funciones de árboles
##############################################################################

class Tree(object):
    def __init__(self, label, left, right):
        self.label = label
        self.left = left
        self.right = right

def Inorder(f):
    # Imprime una formula como cadena dada una formula como arbol
    # Input: tree, que es una formula de logica proposicional
    # Output: string de la formula
	if f.right == None:
		return f.label
	elif f.label == '-':
		return f.label + Inorder(f.right)
	else:
		return "(" + Inorder(f.left) + f.label + Inorder(f.right) + ")"


def StringtoTree(A):
	conectivos = ['O', 'Y', '>']
	pila = []
    
	for c in A:
		if c in letrasProposicionales:
			pila.append(Tree(c, None, None))
		elif c == '-':
			formulaAux = Tree(c, None, pila[-1])
			del pila[-1]
			pila.append(formulaAux)
		elif c in conectivos:
			formulaAux = Tree(c, pila[-1], pila[-2])
			del pila[-1]
			del pila[-1]
			pila.append(formulaAux)
	return pila[-1]


def enFNC(A):
    assert(len(A)==4 or len(A)==7), u"Fórmula incorrecta!"
    B = ''
    p = A[0]
    if "-" in A:
        q = A[-1]
        B = "-"+p+"O-"+q+"Y"+p+"O"+q
    elif "Y" in A:
        q = A[3]
        r = A[5]
        B = q+"O-"+p+"Y"+r+"O-"+p+"Y-"+q+"O-"+r+"O"+p
    elif "O" in A:
        q = A[3]
        r = A[5]
        B = "-"+q+"O"+p+"Y-"+r+"O"+p+"Y"+q+"O"+r+"O-"+p
    elif ">" in A:
        q = A[3]
        r = A[5]
        B = q+"O"+p+"Y-"+r+"O"+p+"Y-"+q+"O"+r+"O-"+p
    else:
        print(u'Error enENC(): Fórmula incorrecta!')
    return B


def Tseitin(A, letrasProposicionalesA):
    letrasProposicionalesB = [chr(x) for x in range(290, 1200)]
    assert(not bool(set(letrasProposicionalesA) & set(letrasProposicionalesB))), u"¡Hay letras proposicionales en común!"
    atomos = letrasProposicionalesA + letrasProposicionalesB
    L = []
    pila = []
    i = -1
    s = A[0]

    while len(A) > 0:
        if s in atomos and len(pila) > 0 and pila[-1] == "-":
            i += 1
            atomo = letrasProposicionalesB[i]
            pila = pila[:-1]
            pila.append(atomo)
            L.append(atomo + "=" + "-" + s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]
        elif s == ")":
            w = pila[-1]
            O = pila[-2]
            v = pila[-3]
            pila = pila[:len(pila) - 4]
            i += 1
            atomo = letrasProposicionalesB[i]
            L.append(atomo + "=" + "(" + v + O + w + ")")
            s = atomo
        else:
            pila.append(s)
            A = A[1:]
            if len(A) > 0:
                s = A[0]

    B = ""
    if i < 0:
        atomo = pila[-1]
    else:
        atomo = letrasProposicionalesB[i]

    for X in L:
        Y = enFNC(X)
        B += "Y" + Y

    B = atomo + B
    return B


def Clausula(C):
    L = []
    while len(C) > 0:
        s = C[0]
        if s == "O":
            C = C[1:]
        elif s == "-":
            literal = s + C[1]
            L.append(literal)
            C = C[2:]
        else:
            L.append(s)
            C = C[1:]
    return L

def formaClausal(A):
    L = []
    i = 0
    while len(A) > 0:
        if i >= len(A):
            L.append(Clausula(A))
            A = []
        else:
            if A[i] == "Y":
                L.append(Clausula(A[:i]))
                A = A[i + 1:]
                i = 0
            else:
                i += 1
    return L

#La sustitucion de las letras proposicionales 
#Ā = p2
#ā = r2
#Ă = v2
#ă = x2 
#Ą = p4
#ą = r4
#Ć = v4
#ć = x4
#Ĉ = p6
#ĉ = r6
#Ċ = v6
#ċ = x6
#Č = p8
#č = r8
#Ď = v8
#ď = x8 
#Đ = q1
#đ = s1
#Ē = u1
#ē = w1
#Ĕ = q3
#ĕ = s3
#Ė = u3
#ė = w3
#Ę = q7
#ę = s7 
#Ě = u7
#ě = w7
#Ĝ = q9
#ĝ = s9 
#Ğ = u9
#ğ = w9 
#Ġ = t5
    