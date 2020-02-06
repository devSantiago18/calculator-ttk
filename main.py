from tkinter import * 

from model.Calculadora import *
from cal_values import *

# Var Globales
num_total = 0
var_first = True # variable que indica si es la primera operacion en realizarse
TAM_BOTON_NUMERO = 50
final_operation = ''


#methods
def cero():
    result.set(result.get() + '0')
    

def uno():
    result.set(result.get() + '1')
    
    
def dos():
    result.set(result.get() + '2')
    
def tres():
    result.set(result.get() + '3')
    
def cuatro():
    result.set(result.get() + '4')
    
def cinco():
    result.set(result.get() + '5')
    
def seis():
    result.set(result.get() + '6')
    
def siete():
    result.set(result.get() + '7')
    
def ocho():
    result.set(result.get() + '8')
    
def nueve():
    result.set(result.get() + '9')
    

    
def concat():
    """ funcion que concatena la lista de numeros y lo escribe en el label del resultado """
    pass


def clear():
    """ Clear the labels """ 
    num1.set(' ')
    num2.set(' ')
    var_first = True

def sumar():
    """Pues suma """
    global num_total
    global final_operation
    global var_first
    num_total += int(result.get())
    print('n t {}'.format(num_total))
    final_operation = '+'
    result.set("")
    var_first = False
        
def restar():
    """pues resta """    
    global num_total
    global final_operation
    global var_first
    if var_first:
        num_total = int(result.get())
        var_first = False
    else:
        num_total -= int(result.get())
    final_operation = '-'
    print('n t {}'.format(num_total))
    result.set("")

def multiplicar():
    """pues multiplica """    
    global num_total
    global var_first
    global final_operation
    if var_first:
        num_total = int(result.get())
        var_first = False
    else:
        num_total = num_total * int(result.get())
    print('n t {}'.format(num_total))
    final_operation = '*'
    result.set("")
        
def dividir():
    """pues divide """    
    global num_total
    global var_first
    global final_operation
    if var_first:
        num_total = int(result.get())
        var_first = False
    else:
        num_total = int( num_total / int(result.get()) ) 
    print('n t {}'.format(num_total))
    final_operation = '/'
    result.set("")

def cls_method():
    """clean all data """ 
    global num_total
    global var_first
    num_total = 0 
    var_first = True
    result.set('')
    
def igual():
    """ get final result """
    global num_total
    global final_operation
    global var_first
    if final_operation == '+':
        sumar()
    if final_operation == '-':
        restar()
    if final_operation == '*':
        multiplicar()
    if final_operation == '/':
        dividir() 
    result.set(str(num_total))
    var_first = True
    num_total = 0



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
frame = Frame(root , width=480 , height=340)
frame.pack(fill='both' , expand=1)
frame.config(bg='lightblue')
frame.config(bd=25)


#Elements
Entry(frame , state=DISABLED, textvariable=result).place(x=15, y=10, width=400 , height=30)



Button(root, text='1' , command=uno).place(x=40, y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='2' , command=dos).place(x=40, y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='3' , command=tres).place(x=40,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='4' , command=cuatro).place(x=110,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='5' , command=cinco).place(x=110,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='6' , command=seis).place(x=110,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='7' , command=siete).place(x=180,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='8' , command=ocho).place(x=180,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='9' , command=nueve).place(x=180,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='0' , command=cero).place(x=40,y=280,width=190 , height=TAM_BOTON_NUMERO)


Button(root, text='+' , command=sumar).place(x=260,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='-' , command=restar).place(x=260,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)
Button(root, text='*' , command=multiplicar).place(x=260,y=220,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='/' , command=dividir).place(x=330,y=100,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO)

Button(root, text='Cls' , command=cls_method).place(x=330,y=160,width=TAM_BOTON_NUMERO , height=TAM_BOTON_NUMERO + 60)
Button(root, text='=' , command=igual).place(x=260,y=280,width=190 , height=TAM_BOTON_NUMERO)


#Button(root, text='sumar' , command=sumar).grid(row=4,column=0 , pady=5)
#Button(root, text='restar' , command=restar).grid(row=4,column=1 ,pady=5)
#Button(root, text='multiplicar' , command=multiplicar).grid(row=4,column=2, pady=5)

root.mainloop()