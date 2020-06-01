#Codigo Realizado por:
    # Nicolas Otero
    # Santiago Alvarez Barbosa 

print("Importando paquetes...")
import Logic_Defenitions as ld
import DPLL as dpll
import Visualizacion_Cuadrado_Magico as vcm
print("Importacion exitosa!")
print("\n")

letrasProposicionales = [chr(x) for x in range(256, 289)]
conectoresBinarios = ["O", "Y", ">", "<->"]
negacion = ["-"]

interps = []
aux = {}

print("Estaremos trabajando con estas Letras proposicionales: ", letrasProposicionales)

#A continuacion se encuentran la representacion de las reglas mediante logica proposicional 

#R1: En cada casilla debe haber un solo numero
a1 = "Đđ-Ē-ē-YYYĐ-đĒ-ē-YYYĐ-đ-Ēē-YYYĐ-đ-Ē-ēYYYOOO"
a2 = "ăĂ-ā-Ā-YYYă-Ăā-Ā-YYYă-Ă-āĀ-YYYă-Ă-ā-ĀYYYOOO"
a3 = "Ĕĕ-Ė-ė-YYYĔ-ĕĖ-ė-YYYĔ-ĕ-Ėė-YYYĔ-ĕ-Ė-ėYYYOOO"
a4 = "ćĆ-ą-Ą-YYYć-Ćą-Ą-YYYć-Ć-ąĄ-YYYć-Ć-ą-ĄYYYOOO"
a5 = "Ġ"
a6 = "ċĊ-ĉ-Ĉ-YYYċ-Ċĉ-Ĉ-YYYċ-Ċ-ĉĈ-YYYċ-Ċ-ĉ-ĈYYYOOO"
a7 = "Ęę-Ě-ě-YYYĘ-ęĚ-ě-YYYĘ-ę-Ěě-YYYĘę-Ě-ěYYYOOO"
a8 = "Ď-č-Č-YYYď-Ďč-Č-YYYď-Ď-čČ-YYYď-Ď-č-ČYYYOOO"
a9 = "Ĝĝ-Ğ-ğ-YYYĜ-ĝĞ-ğ-YYYĜ-ĝ-Ğğ-YYYĜ-ĝ-Ğ-ğYYYOOO"

Regla_1 = "Ğ-ĝ-Ĝ-ğYYYğ-ĝ-Ĝ-ĞYYYğ-Ğ-Ĝ-ĝYYYğ-Ğ-ĝ-ĜYYYOOOĎ-č-Č-ďYYYď-č-Č-ĎYYYď-Ď-Č-čYYYď-Ď-č-ČYYYOOOĚ-ę-Ę-ěYYYě-ę-Ę-ĚYYYě-Ě-Ę-ęYYYě-Ě-ę-ĘYYYOOOĊ-ĉ-Ĉ-ċYYYċ-ĉ-Ĉ-ĊYYYċ-Ċ-Ĉ-ĉYYYċ-Ċ-ĉ-ĈYYYOOOĠĆ-ą-Ą-ćYYYć-ą-Ą-ĆYYYć-Ć-Ą-ąYYYć-Ć-ą-ĄYYYOOOĖ-ĕ-Ĕ-ėYYYė-ĕ-Ĕ-ĖYYYė-Ė-Ĕ-ĕYYYė-Ė-ĕ-ĔYYYOOOĂ-ā-Ā-ăYYYă-ā-Ā-ĂYYYă-Ă-Ā-āYYYă-Ă-ā-ĀYYYOOOĒ-đ-Đ-ēYYYē-đ-Đ-ĒYYYē-Ē-Đ-đYYYē-Ē-đ-ĐYYYOOOYYYYYYYY"


#R2: No se pueden repetir numeros dentro de la matriz
b1 = "ğě-ė-ē-YYYğ-ěė-ē-YYYğ-ě-ėē-YYYğ-ě-ė-ēYYYOOO"
b2 = "ČĈ-Ą-Ā-YYYČ-ĈĄ-Ā-YYYČ-Ĉ-ĄĀ-YYYČ-Ĉ-Ą-ĀYYYOOO"
b3 = "ĜĘ-Ĕ-Đ-YYYĜ-ĘĔ-Đ-YYYĜ-Ę-ĔĐ-YYYĜ-Ę-Ĕ-ĐYYYOOO"
b4 = "čĉ-ą-ā-YYYč-ĉą-ā-YYYč-ĉ-ąā-YYYč-ĉ-ą-āYYYOOO"
b5 = "Ġ"
b6 = "ĝę-ĕ-đ-YYYĝ-ęĕ-đ-YYYĝ-ę-ĕđ-YYYĝ-ę-ĕ-đYYYOOO"
b7 = "ĎĊ-Ć-Ă-YYYĎ-ĊĆ-Ă-YYYĎ-Ċ-ĆĂ-YYYĎ-Ċ-Ć-ĂYYYOOO"
b8 = "ĞĚ-Ė-Ē-YYYĞ-ĚĖ-Ē-YYYĞ-Ě-ĖĒ-YYYĞ-Ě-Ė-ĒYYYOOO"
b9 = "ďċ-ć-ă-YYYď-ċć-ă-YYYď-ċ-ćă-YYYď-ċ-ć-ăYYYOOO"
Regla_2 = "ďċ-ć-ă-YYYď-ċć-ă-YYYď-ċ-ćă-YYYď-ċ-ć-ăYYYOOOĞĚ-Ė-Ē-YYYĞ-ĚĖ-Ē-YYYĞ-Ě-ĖĒ-YYYĞ-Ě-Ė-ĒYYYOOOĎĊ-Ć-Ă-YYYĎ-ĊĆ-Ă-YYYĎ-Ċ-ĆĂ-YYYĎ-Ċ-Ć-ĂYYYOOOĝę-ĕ-đ-YYYĝ-ęĕ-đ-YYYĝ-ę-ĕđ-YYYĝ-ę-ĕ-đYYYOOOĠčĉ-ą-ā-YYYč-ĉą-ā-YYYč-ĉ-ąā-YYYč-ĉ-ą-āYYYOOOĜĘ-Ĕ-Đ-YYYĜ-ĘĔ-Đ-YYYĜ-Ę-ĔĐ-YYYĜ-Ę-Ĕ-ĐYYYOOOČĈ-Ą-Ā-YYYČ-ĈĄ-Ā-YYYČ-Ĉ-ĄĀ-YYYČ-Ĉ-Ą-ĀYYYOOOğě-ė-ē-YYYğ-ěė-ē-YYYğ-ě-ėē-YYYğ-ě-ė-ēYYYOOOYYYYYYYY"


#R3: Cada fila, columna y diagonal debe sumar a 15
ms1 = "ĜďęĊĠąĖĀēYYYYYYYY"
ms2 = "ĜĎĚċĠĄĕāēYYYYYYYY"
ms3 = "ĝčěċĠĄĔĂĒYYYYYYYY"
ms4 = "ĞČěĊĠąĔăđYYYYYYYY"
ms5 = "ğČĚĉĠĆĕăĐYYYYYYYY"
ms6 = "ğčęĈĠćĖĂĐYYYYYYYY"
ms7 = "ĞĎĘĈĠćėāđYYYYYYYY"
ms8 = "ĝďĘĉĠĆėĀĒYYYYYYYY"
Regla_3 = "ĝďĘĉĠĆėĀĒYYYYYYYYĞĎĘĈĠćėāđYYYYYYYYğčęĈĠćĖĂĐYYYYYYYYğČĚĉĠĆĕăĐYYYYYYYYĞČěĊĠąĔăđYYYYYYYYĝčěċĠĄĔĂĒYYYYYYYYĜĎĚċĠĄĕāēYYYYYYYYĜďęĊĠąĖĀēYYYYYYYYOOOOOOO"


#La combinacion de todas las reglas:
Regla_max = Regla_1 + Regla_2 + Regla_3 + "YY"

#El proceso para encontrar que interpretacion hace nuestra regla max satisfasible
arbol = ld.StringtoTree(Regla_max)
formula = ld.Inorder(arbol)
print("La formaula en modo inorder es: ", formula)
print("\n")
tseitin = ld.Tseitin(formula, letrasProposicionales)
causal = ld.formaClausal(tseitin)
copy = causal[:]
count=0
for x in copy:
    copy[count] = ''
    for y in x:
       copy[count]  = copy[count] + y
    count+=1
Dpll = dpll.DPLL(copy,{})
print("DPLL DONE!")
print(Dpll)
interpretaciones = Dpll[1]
keys = interpretaciones.keys()
no_importa = [x for x in interpretaciones if x not in letrasProposicionales]    
for key in[x for x in interpretaciones if x not in letrasProposicionales]: del interpretaciones[key]
print("\n")
print("Interpretaciones que nos importan! ", interpretaciones)

vcm.dibujar_tablero(interpretaciones, 1)
print("DONE! el codigo ha terminado, y pudes mirar el cuadrado magico que generó!")





