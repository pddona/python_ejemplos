#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7
    
import random
import math
import time

def main():

    #VENTANA
    window =  Tk()
    window.title('Bubble Blaster')

    #CANVAS
    HEIGHT = 500
    WIDTH = 800
    c = Canvas(window, width=WIDTH, height=HEIGHT, bg='lightblue')
    c.pack()

    #NAVE ESPACIAL
    SHIP_RADIUS = 15
    MID_X = WIDTH / 2
    MID_Y = HEIGHT / 2
    icono = PhotoImage(file='player.png')
    ship = c.create_image(MID_X,MID_Y,image=icono)
    c.move(ship,MID_X,MID_Y)
    SHIP_SPEED = 2 #################### ajustar


    ###  REGISTRO DE TECLAS PULSADAS
    ######################################################################
    teclas_abajo = {'a':False,'d':False,'w':False,'s':False}##############
    def add_key(event): # AÑADIR TECLA a la lista de teclas pulsadas
        if event.keysym == 'a':
            teclas_abajo['a']=True   
        elif event.keysym == 'd':
            teclas_abajo['d']=True
        elif event.keysym == 'w':
            teclas_abajo['w']=True
        elif event.keysym == 's':
            teclas_abajo['s']=True
        #move_ship()
        



    def delete_key(event): # ELIMINAR TECLAS de la lista de teclas pulsadas
        if event.keysym == 'a':
            teclas_abajo['a']=False   
        elif event.keysym == 'd':
            teclas_abajo['d']=False
        elif event.keysym == 'w':
            teclas_abajo['w']=False
        elif event.keysym == 's':
            teclas_abajo['s']=False
        #move_ship()
        
    c.bind_all('<KeyPress>',add_key)  # EVENTO tecla pulsada
    c.bind_all('<KeyRelease>',delete_key) #EVENTO tecla soltada

    def move_ship():   # FUNCION   MOVER NAVE ESPACIAL
        if teclas_abajo['w'] and teclas_abajo['d']:
            c.move(ship,SHIP_SPEED,-SHIP_SPEED)
           
        elif teclas_abajo['w'] and teclas_abajo['a']:
            c.move(ship,-SHIP_SPEED,-SHIP_SPEED)
            
        elif teclas_abajo['s'] and teclas_abajo['a']:
            c.move(ship,-SHIP_SPEED,SHIP_SPEED)
            
        elif teclas_abajo['s'] and teclas_abajo['d']:
            c.move(ship,SHIP_SPEED,SHIP_SPEED)
              
        elif teclas_abajo['w']:
            c.move(ship,0,-SHIP_SPEED)
            
        elif teclas_abajo['s']:
            c.move(ship,0,SHIP_SPEED)
            
        elif teclas_abajo['a']:
            c.move(ship,-SHIP_SPEED,0)
            
        elif teclas_abajo['d']:
            c.move(ship,SHIP_SPEED,0)
            
    #################################################################################       
    # POMPAS
    bubble_id = list()  #Lista vacia  []
    bubble_radius = list() #Lista vacia  []
    bubble_speed = list() #Lista vacia  []
    MIN_BUBBLE_RADIUS = 10
    MAX_BUBBLE_RADIUS = 30
    MAX_BUBBLE_SPEED = 10
    GAP = 100 # margen a la derecha fuera de la pantalla

    def create_bubble():  # CREAR POMPAS
        x = WIDTH + GAP
        y = random.randint(0, HEIGHT)
        r = random.randint(MIN_BUBBLE_RADIUS, MAX_BUBBLE_RADIUS)
        micolor = lambda: random.randint(0,255) ###COLORES aleatorios
        micolor_text= '#%02X%02X%02X' % (micolor(),micolor(),micolor()) # COlor hexadecimal   #FFFFFF
        id1 = c.create_oval(x-r, y-r, x+r, y+r, outline=micolor_text ,width=3 , fill=micolor_text)
        bubble_id.append(id1)
        bubble_radius.append(r)
        bubble_speed.append(random.randint(1,MAX_BUBBLE_SPEED))

    def move_bubbles():  # MOVER POMPAS
        for i in range(len(bubble_id)):
            c.move(bubble_id[i], -1*bubble_speed[i], 0)
    
    def get_coords(id): # Obtener situacion POMPA
        pos = c.coords(id) # x1,y1,x2,y2     0,1,2,3
        x = (pos[0] + pos[2]) / 2
        y = (pos[1] + pos[3]) / 2
        return x, y
        
    def get_coords_nave(id): # Obtener situacion NAVE
        pos = c.coords(id) # x1,y1  0,1
        x = (pos[0])
        y = (pos[1] )
        return x, y	
		

    def del_bubble(id): # ELIMINAR POMPAS colisionadas
        del bubble_radius[id] #  del  borrar de la lista
        del bubble_speed[id]
        c.delete(bubble_id[id]) # eliminar del CANVAS
        del bubble_id[id]

    def clean_up_bubbles(): # ELIMINAR POMPAS por la izquierda
        for id in range(len(bubble_id)-1,-1,-1):
            x,y = get_coords(bubble_id[id])
            if x < -GAP: # si se sale por la izquierda de la pantalla
                del_bubble(id)

    
    def distance(nave,id2):  # DISTANCIA    nave a pompa
        x1, y1 = get_coords_nave(nave)
        x2, y2 = get_coords(id2)
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    
    def collision(): # COLISIONES
        points = 0
        for id in range(len(bubble_id)-1,-1,-1):
            d = distance(ship, bubble_id[id])
            b  = SHIP_RADIUS + bubble_radius[id]
            if d < b:
                points += bubble_radius[id] + bubble_speed[id]
                del_bubble(id)
        return points
    
    # INFORMACION EN PANTALLA
    c.create_text(50,30,text='TIME',fill='black')
    c.create_text(150,30,text='SCORE',fill='black')
    time_text = c.create_text(50,50,fill='black')
    score_text = c.create_text(150,50,fill='black')

    def show_score(score): # Mostrar marcador
        c.itemconfig(score_text,text=str(score))

    def show_time(time_left): # Mostrar tiempo
        c.itemconfig(time_text, text=str(time_left))

    # VARIABLES    
    BUBBLE_CHANCE = 10
    TIME_LIMIT = 15 # cada 1000 puntos añadimos tiempo
    BONUS_SCORE = 1000
    score = 0
    bonus = 0
    end = time.time() + TIME_LIMIT
    
    ####################################  MAIN GAME LOOP ##################
    # BUCLE PRINCIPAL DEL JUEGO 
    while time.time() < end:
        if random.randint(1, BUBBLE_CHANCE) == 1:
            create_bubble()
        move_bubbles()                           
        clean_up_bubbles()
        score += collision()                       # Actualizar puntos
        if (int(score / BONUS_SCORE)) > bonus:
            bonus += 1
            end += TIME_LIMIT
        show_score(score)                        # Mostrar puntos
        show_time(int(end - time.time()))  # Mostrar TIEMPO
        move_ship() ####### MOVER NAVE   solución para darle fluidez al movimiento de la nave
        window.update() ##### IMPORTANTE PARA VER LA VENTANA en cada fotograma
        
    #####################################################################


    # FIN JUEGO
    c.create_text(MID_X, MID_Y, text='GAME OVER', fill='black',
            font=('Helvetica', 30))
    c.create_text(MID_X, MID_Y + 30, text='Score: ' + str(score),
            fill='black')
    c.create_text(MID_X, MID_Y + 45, text='Bonus Time: ' +
            str(bonus*TIME_LIMIT), fill='black')
    

    
    window.mainloop() # Ventana principal
    
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
