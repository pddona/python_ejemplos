#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7

	
def main():

    #Crear y configurar ventana principal
    window = Tk() 
    window.title("Menús")
    
    ######################################  IMC  ######################################    
    def indice_imc():
        nuevaventana = Toplevel(window)# Toplevel es un widget que crea una pop-up window     

        #widgets
        titulo = Label(nuevaventana, text="CÁLCULO DEL ÍNDICE DE MASA CORPORAL") 
        titulo.grid(row=0,column=0)
        
        #Primer número 
        lbl_1 = Label(nuevaventana, text="Peso en Kg")         
        lbl_1.grid(column=0, row=1)  
        numero_1 = Entry(nuevaventana,width=10) # Introducir Primer número       
        numero_1.insert(0,0) # Colocar un cero como valor inicial en la primera posición
        numero_1.grid(column=1, row=1) 
         
        #Segundo número
        lbl_2 = Label(nuevaventana, text="Altura en metros")         
        lbl_2.grid(column=0, row=2)
        numero_2 = Entry(nuevaventana,width=10) # Introducir Segundo número   
        numero_2.insert(0,0) # Colocar un cero como valor inicial en la primera posición     
        numero_2.grid(column=1, row=2) 
         
        #Resultado
        label_resultado = Label(nuevaventana, text='IMC')
        label_resultado.grid(column=0, row=3)
        resultado = Label(nuevaventana, text='')
        resultado.grid(column=1, row=3)
        
        # FUNCION que realiza el cálculo,  es llamada por el BOTON 'calcular'  con     'command=imc'
        def imc():
            try:  # Comprobar que los números introducidos son válidos y no son letras
                peso = float( numero_1.get().replace(',', '.') )  # OJO al introducir por teclados números decimales con coma
                altura = float( numero_2.get().replace(',','.') ) # SUSTITUIR COMAS por PUNTOS
                solucion = float(    peso / altura**2   ) 
                resultado.config(text = solucion)# Modificar el contenido del label 'resultado'
            except:
                resultado.config(text ='Debe introducir números válidos')  
            
        #Botón que llama a la función 'media' deifnida arriba         
        calcular = Button(nuevaventana,text='Calcular ICM',command=imc)
        calcular.grid(column=0, row=4)
        '''
        #Botón CERRAR     NO es necesario   La X de la ventana tambien cierra
        destruir = Button(nuevaventana , text = 'Cerrar' , command = nuevaventana.destroy ) # elimina ventana nuevawin
        #  el metodo   widget.destroy() está accesible para cualquier widget
        destruir.grid(column=0, row=5)
        '''  
   
   
    #######################################  MEDIA ARITMETICA  ######################################
    def media_aritmerica(): 
        nuevaventana = Toplevel(window)# Toplevel es un widget que crea una pop-up window 
        #widgets
        titulo = Label(nuevaventana, text="Programa para el cálculo de la media aritmética de dos números") 
        titulo.grid(row=0,column=0)
        
        #Primer número 
        lbl_1 = Label(nuevaventana, text="Primer número")         
        lbl_1.grid(column=0, row=1)  
        numero_1 = Entry(nuevaventana,width=10) # Introducir Primer número       
        numero_1.insert(0,0) # Colocar un cero como valor inicial en la primera posición
        numero_1.grid(column=1, row=1) 
         
        #Segundo número
        lbl_2 = Label(nuevaventana, text="Segundo número")         
        lbl_2.grid(column=0, row=2)
        numero_2 = Entry(nuevaventana,width=10) # Introducir Segundo número   
        numero_2.insert(0,0) # Colocar un cero como valor inicial en la primera posición     
        numero_2.grid(column=1, row=2) 
         
        #Resultado
        label_resultado = Label(nuevaventana, text='Resultado')
        label_resultado.grid(column=0, row=3)
        resultado = Label(nuevaventana, text='')
        resultado.grid(column=1, row=3)
        
        # FUNCION que realiza el cálculo,  es llamada por el BOTON 'calcular'  con     'command=media'
        def media():
            try:  # Comprobar que los números introducidos son válidos y no son letras
                n1= float( numero_1.get().replace(',', '.') )
                n2= float( numero_2.get().replace(',', '.') )
                solucion = float(  n1   +  n2  ) / 2     
                resultado.config(text = solucion)# Modificar el contenido del label 'resultado'
            except:
                resultado.config(text ='Debe introducir números válidos')
            
        #Botón que llama a la función 'media' deifnida arriba         
        calcular = Button(nuevaventana,text='Calcular',command=media)
        calcular.grid(column=0, row=4)
 
 
    
   
    # Crear Nueva Barra de Menús
    menubar = Menu(window) 

    # Crear nueva entrada de menú   'HERRAMINETAS'
    toolmenu = Menu(menubar, tearoff=0) 
    # filemenu = Menu(menubar)
    # si tearoff no es 0  el menu se puede separar desde el primer elemento del menú   - - - - - -
    toolmenu.add_command(label="Media aritmética",        command=media_aritmerica)
    toolmenu.add_command(label="Índice de masa corporal",       command=indice_imc)              
    toolmenu.add_separator() # línea separadora
    toolmenu.add_command(label="Salir", command=window.destroy)
    menubar.add_cascade(label="Herramientas", menu=toolmenu) # Nombre del Desplegable superior del menú

        

    window.config(menu = menubar) # Asignar a la ventana principal el menu creado
       
    #Bucle principal de la ventana 
    window.mainloop()

        
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
