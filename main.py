from tkinter import * 

from model.Calculadora import *
from cal_values import *

# Var Globales
array_nums = []
TAM_BOTON_NUMERO = 50

#methods
def cero():
    array_nums.append(0)
def uno():
    array_nums.append(1)
def dos():
    array_nums.append(2)
def tres():
    array_nums.append(3)
def cuatro():
    array_nums.append(4)
def cinco():
    array_nums.append(5)
def seis():
    array_nums.append(6)
def siete():
    array_nums.append(7)
def ocho():
    array_nums.append(8)
def nueve():
    array_nums.append(9)

    


def clear():
    """ Clear the labels """ 
    num1.set(' ')
    num2.set(' ')

def sumar():
    """Pues suma """
    try:
        result.set(str(suma(int(num1.get()), int(num2.get()) )) )
    except Exception as e: # por planear
        result.set("Por favor introduzca solo numeros enteros")
        clear()    
    finally:
        clear()
        
def restar():
    """pues resta """    
    try:
        result.set(str(resta(int(num1.get()), int(num2.get()) )) )
    except Exception as e: # por planear
        result.set("Por favor introduzca solo numeros enteros")
        clear()
    finally:
        clear()

def multiplicar():
    """pues multiplica """    
    try:
        result.set( str(mutiplicacion(int(num1.get()), int(num2.get())) ) )
    except Exception as e: # por planear
        result.set("Por favor introduzca solo numeros enteros")
        clear()    
    finally:
        clear()
        

        
    
root = Tk()
root.config(bd=15)
root.resizable(0,0)
root.title('Calculadora')
#tres variables para manejar los numeros y el resultado
num1 = StringVar()
num2 = StringVar()
result = StringVar()

#Label(root , text='Num 1').grid(row=0,column=0)
#Entry(root , justify=CENTER , textvariable=num1 ).pack(side=TOP)

#Label(root , text='Num 2').grid(row=1,column=0)
#Entry(root , justify=CENTER , textvariable=num2 ).grid(row=1,column=1)
#Label(root).grid(row=1) #separador

#Label(root).grid(row=2) #separador
frame = Frame(root , width=480 , height=320)
frame.pack(fill='both' , expand=1)
frame.config(bg='lightblue')
frame.config(bd=25)


#Elements
Entry(frame , state=DISABLED, textvariable=result).place(x=15, y=10, width=400 , height=30)



Button(root, text='1' , command=uno).place(x=40, y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='2' , command=dos).place(x=40, y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='3' , command=tres).place(x=40,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='4' , command=uno).place(x=110,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='5' , command=dos).place(x=110,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='6' , command=tres).place(x=110,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='7' , command=uno).place(x=180,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='8' , command=dos).place(x=180,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='9' , command=tres).place(x=180,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='9' , command=tres).place(x=180,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

#Button(root, text='sumar' , command=sumar).grid(row=4,column=0 , pady=5)
#Button(root, text='restar' , command=restar).grid(row=4,column=1 ,pady=5)
#Button(root, text='multiplicar' , command=multiplicar).grid(row=4,column=2, pady=5)

root.mainloop()