#-*-coding: utf-8-*-

# Visualizacion de tableros de ajedrez 3x3 a partir de
# una lista de literales. Cada literal representa una casilla con el numero que se debe encontrar ahí;

# Salida: archivo tablero_%i.png, donde %i es un número natural

#################
# importando paquetes para dibujar
print("Importando paquetes...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
print("Listo!")

def dibujar_tablero(f, n):
    # Visualiza un tablero dada una formula f
    # Input:
    #   - f, un diccionario de literales
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el tablero
    step = 1./3
    tangulos = []
    # Creo los cuadrados claros en el tablero
    tangulos.append(patches.Rectangle(\
                                    (0, step), \
                                    step, \
                                    step,\
                                    facecolor='white')\
                                    )
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(step, 2 * step), step, step],\
            facecolor='white'))
    # Creo los cuadrados oscuros en el tablero
    tangulos.append(patches.Rectangle(*[(2 * step, 2 * step), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(0, 2 * step), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='white'))
    tangulos.append(patches.Rectangle(*[(0, 0), step, step],\
            facecolor='white'))

    # Creo las líneas del tablero
    for j in range(3):
        locacion = j * step
        # Crea linea horizontal en el rectangulo
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical en el rectangulo
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))

    for t in tangulos:
        axes.add_patch(t)

    # Cargando imagenes con los numeros 1-9
    arr_img = plt.imread("UNO.png", format='png')
    imagebox1 = OffsetImage(arr_img, zoom=0.05)
    imagebox1.image.axes = axes
    
    arr_img = plt.imread("DOS.png", format='png')
    imagebox2 = OffsetImage(arr_img, zoom=0.06)
    imagebox2.image.axes = axes
    
    arr_img = plt.imread("TRES.png", format='png')
    imagebox3 = OffsetImage(arr_img, zoom=0.05)
    imagebox3.image.axes = axes
    
    arr_img = plt.imread("CUATRO.png", format='png')
    imagebox4 = OffsetImage(arr_img, zoom=0.1)
    imagebox4.image.axes = axes
    
    arr_img = plt.imread("CINCO.png", format='png')
    imagebox5 = OffsetImage(arr_img, zoom=0.04)
    imagebox5.image.axes = axes
    
    arr_img = plt.imread("SEIS.png", format='png')
    imagebox6 = OffsetImage(arr_img, zoom=0.03)
    imagebox6.image.axes = axes
    
    arr_img = plt.imread("SIETE.png", format='png')
    imagebox7 = OffsetImage(arr_img, zoom=0.03)
    imagebox7.image.axes = axes
    
    arr_img = plt.imread("OCHO.png", format='png')
    imagebox8 = OffsetImage(arr_img, zoom=0.04)
    imagebox8.image.axes = axes
    
    arr_img = plt.imread("NUEVE.png", format='png')
    imagebox9 = OffsetImage(arr_img, zoom=0.05)
    imagebox9.image.axes = axes


    # Creando las direcciones en la imagen de acuerdo a literal
    direcciones = {}
    direcciones[1] = [0.165, 0.835]
    direcciones[2] = [0.5, 0.835]
    direcciones[3] = [0.835, 0.835]
    direcciones[4] = [0.165, 0.5]
    direcciones[5] = [0.5, 0.5]
    direcciones[6] = [0.835, 0.5]
    direcciones[7] = [0.165, 0.165]
    direcciones[8] = [0.5, 0.165]
    direcciones[9] = [0.835, 0.165]
    
    direcciones[10] = [0.165, 0.835]
    direcciones[11] = [0.5, 0.835]
    direcciones[12] = [0.835, 0.835]
    direcciones[13] = [0.165, 0.5]
    direcciones[14] = [0.835, 0.5]
    direcciones[15] = [0.165, 0.165]
    direcciones[16] = [0.5, 0.165]
    direcciones[17] = [0.835, 0.165]
    
    direcciones[18] = [0.165, 0.835]
    direcciones[19] = [0.5, 0.835]
    direcciones[20] = [0.835, 0.835]
    direcciones[21] = [0.165, 0.5]
    direcciones[22] = [0.835, 0.5]
    direcciones[23] = [0.165, 0.165]
    direcciones[24] = [0.5, 0.165]
    direcciones[25] = [0.835, 0.165]
    
    direcciones[26] = [0.165, 0.835]
    direcciones[27] = [0.5, 0.835]
    direcciones[28] = [0.835, 0.835]
    direcciones[29] = [0.165, 0.5]
    direcciones[30] = [0.835, 0.5]
    direcciones[31] = [0.165, 0.165]
    direcciones[32] = [0.5, 0.165]
    direcciones[33] = [0.835, 0.165]
    
    
    for l in f:
        if f['Ā'] == 1:
            ab = AnnotationBbox(imagebox1, direcciones[int(2)], frameon=False)
            axes.add_artist(ab) 
        if f['ā'] == 1:
            ab = AnnotationBbox(imagebox3, direcciones[int(2)], frameon=False)
            axes.add_artist(ab) 
        if f['Ă'] == 1:
            ab = AnnotationBbox(imagebox7, direcciones[int(2)], frameon=False)
            axes.add_artist(ab) 
        if f['ă'] == 1:
            ab = AnnotationBbox(imagebox9, direcciones[int(2)], frameon=False)
            axes.add_artist(ab) 
            
        if f['Ą'] == 1:
            ab = AnnotationBbox(imagebox1, direcciones[int(4)], frameon=False)
            axes.add_artist(ab) 
        if f['ą'] == 1:
            ab = AnnotationBbox(imagebox3, direcciones[int(4)], frameon=False)
            axes.add_artist(ab) 
        if f['Ć'] == 1:
            ab = AnnotationBbox(imagebox7, direcciones[int(4)], frameon=False)
            axes.add_artist(ab) 
        if f['ć'] == 1:
            ab = AnnotationBbox(imagebox9, direcciones[int(4)], frameon=False)
            axes.add_artist(ab) 
            
        if f['Ĉ'] == 1:
            ab = AnnotationBbox(imagebox1, direcciones[int(6)], frameon=False)
            axes.add_artist(ab) 
        if f['ĉ'] == 1:
            ab = AnnotationBbox(imagebox3, direcciones[int(6)], frameon=False)
            axes.add_artist(ab) 
        if f['Ċ'] == 1:
            ab = AnnotationBbox(imagebox7, direcciones[int(6)], frameon=False)
            axes.add_artist(ab) 
        if f['ċ'] == 1:
            ab = AnnotationBbox(imagebox9, direcciones[int(6)], frameon=False)
            axes.add_artist(ab) 
            
        if f['Č'] == 1:
            ab = AnnotationBbox(imagebox1, direcciones[int(8)], frameon=False)
            axes.add_artist(ab) 
        if f['č'] == 1:
            ab = AnnotationBbox(imagebox3, direcciones[int(8)], frameon=False)
            axes.add_artist(ab) 
        if f['Ď'] == 1:
            ab = AnnotationBbox(imagebox7, direcciones[int(8)], frameon=False)
            axes.add_artist(ab) 
        if f['ď'] == 1:
            ab = AnnotationBbox(imagebox9, direcciones[int(8)], frameon=False)
            axes.add_artist(ab) 
        
        if f['Ġ'] == 1:
            ab = AnnotationBbox(imagebox5, direcciones[int(5)], frameon=False)
            axes.add_artist(ab) 
            
        if f['Đ'] == 1:
            ab = AnnotationBbox(imagebox2, direcciones[int(1)], frameon=False)
            axes.add_artist(ab) 
        if f['đ'] == 1:
            ab = AnnotationBbox(imagebox4, direcciones[int(1)], frameon=False)
            axes.add_artist(ab) 
        if f['Ē'] == 1:
            ab = AnnotationBbox(imagebox6, direcciones[int(1)], frameon=False)
            axes.add_artist(ab) 
        if f['ē'] == 1:
            ab = AnnotationBbox(imagebox8, direcciones[int(1)], frameon=False)
            axes.add_artist(ab)
            
        if f['Ĕ'] == 1:
            ab = AnnotationBbox(imagebox2, direcciones[int(3)], frameon=False)
            axes.add_artist(ab) 
        if f['ĕ'] == 1:
            ab = AnnotationBbox(imagebox4, direcciones[int(3)], frameon=False)
            axes.add_artist(ab) 
        if f['Ė'] == 1:
            ab = AnnotationBbox(imagebox6, direcciones[int(3)], frameon=False)
            axes.add_artist(ab) 
        if f['ė'] == 1:
            ab = AnnotationBbox(imagebox8, direcciones[int(3)], frameon=False)
            axes.add_artist(ab)
            
        if f['Ę'] == 1:
            ab = AnnotationBbox(imagebox2, direcciones[int(7)], frameon=False)
            axes.add_artist(ab) 
        if f['ę'] == 1:
            ab = AnnotationBbox(imagebox4, direcciones[int(7)], frameon=False)
            axes.add_artist(ab) 
        if f['Ě'] == 1:
            ab = AnnotationBbox(imagebox6, direcciones[int(7)], frameon=False)
            axes.add_artist(ab) 
        if f['ě'] == 1:
            ab = AnnotationBbox(imagebox8, direcciones[int(7)], frameon=False)
            axes.add_artist(ab)
            
        if f['Ĝ'] == 1:
            ab = AnnotationBbox(imagebox2, direcciones[int(9)], frameon=False)
            axes.add_artist(ab) 
        if f['ĝ'] == 1:
            ab = AnnotationBbox(imagebox4, direcciones[int(9)], frameon=False)
            axes.add_artist(ab) 
        if f['Ğ'] == 1:
            ab = AnnotationBbox(imagebox6, direcciones[int(9)], frameon=False)
            axes.add_artist(ab) 
        if f['ğ'] == 1:
            ab = AnnotationBbox(imagebox8, direcciones[int(9)], frameon=False)
            axes.add_artist(ab)
            
    #plt.show()
    fig.savefig("tablero_" + str(n) + ".png")
    
Ā = 1 
Ą = 2
Ĉ = 3
Č = 4
ā = 6 
ą = 7
ĉ = 8
č = 9
Ă = 10 
Ć = 11
Ċ = 12
Ď = 13
ă = 14
ć = 15
ċ = 16
ď = 17

Ġ = 5

Đ = 18
Ĕ = 19
Ę = 20
Ĝ = 21
đ = 22
ĕ = 23
ę = 24
ĝ = 25
Ē = 26
Ė = 27
Ě = 28
Ğ = 29
ē = 30
ė = 31
ě = 32
ğ = 33

plt.close("all")
