#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7
	
def main():

        #Crear y configurar ventana principal
        window = Tk() 
        window.title("Entry")         
        #window.geometry('500x150')  # Si queremos un tamaño determinado de ventana

        #widgets
        titulo = Label(window, text="CÁLCULO DEL ÍNDICE DE MASA CORPORAL") 
        titulo.grid(row=0,column=0)
        
        #Primer número 
        lbl_1 = Label(window, text="Peso en Kg")         
        lbl_1.grid(column=0, row=1)  
        numero_1 = Entry(window,width=10) # Introducir Primer número       
        numero_1.insert(0,0) # Colocar un cero como valor inicial en la primera posición
        numero_1.grid(column=1, row=1) 
         
        #Segundo número
        lbl_2 = Label(window, text="Altura en metros")         
        lbl_2.grid(column=0, row=2)
        numero_2 = Entry(window,width=10) # Introducir Segundo número   
        numero_2.insert(0,0) # Colocar un cero como valor inicial en la primera posición     
        numero_2.grid(column=1, row=2) 
         
        #Resultado
        label_resultado = Label(window, text='IMC')
        label_resultado.grid(column=0, row=3)
        resultado = Label(window, text='')
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
        calcular = Button(window,text='Calcular ICM',command=imc)
        calcular.grid(column=0, row=4) 
       

        #Bucle principal de la ventana 
        window.mainloop()

        
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
