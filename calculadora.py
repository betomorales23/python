#Ejercicio de calculadora con tkinter
#Autor: Humberto Morales

from tkinter import * 

ventana = Tk()
ventana.title("Calculadora Mac")

#Entrada de operacion
ing_texto = Entry(ventana, font = ("Calibri 20"))
ing_texto.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

i = 0
#Funciones de operaciones
def click_btn(valor):
    global i
    ing_texto.insert(i,valor)
    i += 1

def borrar_btn():
    ing_texto.delete(0,END)
    i = 0

def resultados():
    ecuacion = ing_texto.get()
    resultado = eval(ecuacion)
    ing_texto.delete(0,END)
    ing_texto.insert(0,resultado)
    i = 0

#Botones

btn1 = Button(ventana, text = "1", width=5, height=2, command= lambda:click_btn(1))
btn2 = Button(ventana, text = "2", width=5, height=2, command= lambda:click_btn(2))
btn3 = Button(ventana, text = "3", width=5, height=2, command= lambda:click_btn(3))
btn4 = Button(ventana, text = "4", width=5, height=2, command= lambda:click_btn(4))
btn5 = Button(ventana, text = "5", width=5, height=2, command= lambda:click_btn(5))
btn6 = Button(ventana, text = "6", width=5, height=2, command= lambda:click_btn(6))
btn7 = Button(ventana, text = "7", width=5, height=2, command= lambda:click_btn(7))
btn8 = Button(ventana, text = "8", width=5, height=2, command= lambda:click_btn(8))
btn9 = Button(ventana, text = "9", width=5, height=2, command= lambda:click_btn(9))
btn0 = Button(ventana, text = "0", width=5, height=2, command= lambda:click_btn(0))

btn_borrar = Button(ventana, text = "AC", width=5, height=2, command=lambda:borrar_btn())
btn_porcentaje = Button(ventana, text = "%", width=5, height=2, command= lambda:click_btn("%"))
btn_masmenos = Button(ventana, text = "+/-", width=5, height=2, command= lambda:click_btn("+/-"))
btn_punto = Button(ventana, text = ".", width=5, height=2, command= lambda:click_btn("."))

btn_div = Button(ventana, text = "/", width=5, height=2, command= lambda:click_btn("/"))
btn_mult = Button(ventana, text = "*", width=5, height=2, command= lambda:click_btn("*"))
btn_sum = Button(ventana, text = "+", width=5, height=2, command= lambda:click_btn("+"))
btn_rest = Button(ventana, text = "-", width=5, height=2, command= lambda:click_btn("-"))
btn_igual = Button(ventana, text = "=", width=5, height=2, command= lambda:resultados())

#Agregamos botones en pantalla
btn_borrar.grid(row=1,column=0, padx=5, pady=5)
btn_masmenos.grid(row=1,column=1, padx=5, pady=5)
btn_porcentaje.grid(row=1,column=2, padx=5, pady=5)
btn_div.grid(row=1, column=3, padx=5, pady=5)
btn7.grid(row=2, column=0, padx=5, pady=5)
btn8.grid(row=2, column=1, padx=5, pady=5)
btn9.grid(row=2, column=2, padx=5, pady=5)
btn_mult.grid(row=2, column=3, padx=5, pady=5)
btn4.grid(row=3, column=0, padx=5, pady=5)
btn5.grid(row=3, column=1, padx=5, pady=5)
btn6.grid(row=3, column=2, padx=5, pady=5)
btn_rest.grid(row=3, column=3, padx=5, pady=5)
btn1.grid(row=4, column=0, padx=5, pady=5)
btn2.grid(row=4, column=1, padx=5, pady=5)
btn3.grid(row=4, column=2, padx=5, pady=5)
btn_sum.grid(row=4, column=3, padx=5, pady=5)
btn0.grid(row=5,column=0, columnspan=2, padx=5, pady=5)
btn_punto.grid(row=5, column=2, padx=5, pady=5)
btn_igual.grid(row=5, column=3, padx=5, pady=5)
ventana.mainloop()
