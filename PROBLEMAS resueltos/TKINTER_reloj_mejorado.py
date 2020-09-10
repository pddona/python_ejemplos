#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter import *     #  python 3.
except:
    from Tkinter import *    #  python 2.7   
 
from datetime import *     # datetime
from math import *           #math


def main():
    #ventana principal
    window=Tk()
    window.title('Canvas')

    #canvas
    anchoCanvas = 400
    altoCanvas = 400
    centroX = anchoCanvas/2
    centroY = altoCanvas/2
    c=Canvas(window,width=anchoCanvas,height=altoCanvas,bg = 'black') # CANVAS
    c.pack()

    # Variables
    angulo_hora = 2*pi/12
    angulo_segundo = 2*pi/60
    angulo_minuto = 2*pi/60
    radio_punto = 10
    radio_reloj = 100
    long_segundero = 95
    long_minutero = 95
    long_horero = 60
    meses = ['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    
    # Dibujar 12 puntos horas
    for h in range(12):
        coseno = cos(h * angulo_hora) 
        seno = sin(h * angulo_hora)
        x_base = coseno * radio_reloj + anchoCanvas/2
        y_base = seno * radio_reloj + altoCanvas/2
        punto = c.create_oval(x_base - radio_punto , y_base - radio_punto, x_base + radio_punto , y_base + radio_punto , fill='white')#coordenadas esquinas superior izquierda e inferior derecha

    #Dibujar las marcas segundos-minutos
    radio_int = 95
    radio_ext = 105
    for a in range(60):
        coseno = cos(a * angulo_segundo) 
        seno = sin(a * angulo_segundo)
        x_base = coseno * radio_int + anchoCanvas/2
        y_base = seno * radio_int + altoCanvas/2
        x_extremo = coseno * radio_ext + anchoCanvas/2
        y_extremo = seno * radio_ext + altoCanvas/2
        marca = c.create_line(x_base  , y_base , x_extremo , y_extremo , fill='white')





    #Crear manecillas todas mirando hacia arriba
    coordenadas_segundero  = [centroX , centroY , centroX , centroY - long_segundero]
    segundero = c.create_line( coordenadas_segundero , fill ='white' , width = 2 , tag ='manecilla')
    #un item puede ser accedido por si ID (segundero) o por algún tag asignado(‘manecilla’) (puede tener más de un tag)

    coordenadas_minutero  = [centroX , centroY , centroX , centroY - long_minutero]
    minutero = c.create_line( coordenadas_minutero , fill ='yellow' , width = 5)
    coordenadas_horero  = [centroX , centroY , centroX , centroY - long_horero]
    horero = c.create_line( coordenadas_horero , fill ='red' , width = 8)
    hora_digital = c.create_text(anchoCanvas/2 , 50 ,text = '00:00:00' , font = ( 'Time' , 30), fill = 'white')
    fecha_digital = c.create_text(anchoCanvas/2 , 350 ,text = '00-00-00' , font = ( 'Time' , 30), fill = 'white')##fecha

 
    # Bucle infinito para mover manecillas y actualizar reloj
    while True:
        ahora = datetime.now()
        microsegundos = ahora.microsecond #### microsegundos
        centesimas = floor(microsegundos/10000) #### math.floor()
        segundos = ahora.second
        minutos = ahora.minute
        horas = ahora.hour
        dia = ahora.day
        mes = ahora.month
        year = ahora.year

        #hora digital
        if horas<10:
            horas_text = '0'+ str(horas)
        else:
            horas_text = str(horas)
        if minutos<10:
            minutos_text = '0'+ str(minutos)
        else:
            minutos_text = str(minutos)
        if segundos<10:
            segundos_text = '0'+ str(segundos)
        else:
            segundos_text = str(segundos)
        if centesimas<10:
            centesimas_text = '0'+ str(centesimas)
        else:
            centesimas_text = str(centesimas)
        c.itemconfigure(hora_digital,text = str(horas_text)+':'+str(minutos_text)+':'+str(segundos_text)+":"+str(centesimas_text)) #itemconfigure
        # hasta centesimas
        c.itemconfigure(fecha_digital,text = str(dia)+'-'+meses[mes]+'-'+str(year)) #FECHA
        

        
        #segundero
        coseno = cos(segundos * angulo_segundo) 
        seno = sin(segundos * angulo_segundo)
        ######### MODIFICAR COORDENADAS DE UN ITEM por su ID
        c.coords(segundero ,centroX , centroY , centroX + long_segundero * seno , centroY - long_segundero * coseno  ) 
        # o por TAG  c.coords(‘manecilla’ ,centroX , centroY , centroX + long_segundero * seno , centroY - long_segundero * coseno  )
        
        #minutero
        coseno = cos(minutos * angulo_minuto) 
        seno = sin(minutos * angulo_minuto)
         ######### MODIFICAR COORDENADAS DE UN ITEM por su ID
        c.coords(minutero ,centroX , centroY , centroX + long_minutero * seno , centroY - long_minutero * coseno  )

        #horero
        coseno = cos(horas * angulo_hora) 
        seno = sin(horas * angulo_hora)       
         ######### MODIFICAR COORDENADAS DE UN ITEM por su ID
        c.coords(horero ,centroX , centroY , centroX + long_horero * seno , centroY - long_horero * coseno  )

        
        window.update()   #actualizar ventana para ver los cambios

    
    window.attributes('-topmost',True)  #   Colocar ventana delante de todas
    window.mainloop()                          #   Bucle visualización ventana principal
        
if __name__ == "__main__":       # Averiguar si se está ejecutando o importando
        main()
