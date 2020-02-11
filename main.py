from tkinter import * 

#  Globals var
num_total = 0
var_first = True # var to detected the first operation
TAM_BOTON = 50
final_operation = '' # last operation

root = Tk()
root.config(bd=15)
root.resizable(0,0)
root.title('Calculadora')

result = StringVar()

frame = Frame(root , width=480 , height=340)
frame.pack(fill='both' , expand=1)
frame.config(bg='lightblue')
frame.config(bd=25)

def set_num(num):
    result.set(result.get() + str(num))

def operation(op):
    global num_total
    global final_operation
    global var_first
    final_operation = op
    print(op)
    if var_first:
        num_total = float(result.get())
        var_first = False
    else:
        if op == '+':
            num_total += float(result.get())
            print('nt {}'.format(num_total))
        if op == '-':
            num_total -= float(result.get())
            print('nt {}'.format(num_total))
        if op == '*':
            num_total = float(num_total) * float(result.get())
            print('nt {}'.format(num_total))
        if op == '/':
            num_total = float( float(num_total) / float(result.get()) ) 
            print('nt {}'.format(num_total))
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
    operation(final_operation)
    result.set(str(num_total))
    var_first = True
    num_total = 0




#Elements
Entry(frame , state=DISABLED, textvariable=result).place(x=15, y=10, width=400 , height=30)

Button(root, text='1' , command=lambda:set_num(1)).place(x=40, y=100,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='2' , command=lambda:set_num(2)).place(x=40, y=160,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='3' , command=lambda:set_num(3)).place(x=40,y=220,width=TAM_BOTON , height=TAM_BOTON)

Button(root, text='4' , command=lambda:set_num(4)).place(x=110,y=100,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='5' , command=lambda:set_num(5)).place(x=110,y=160,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='6' , command=lambda:set_num(6)).place(x=110,y=220,width=TAM_BOTON , height=TAM_BOTON)

Button(root, text='7' , command=lambda:set_num(7)).place(x=180,y=100,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='8' , command=lambda:set_num(8)).place(x=180,y=160,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='9' , command=lambda:set_num(9)).place(x=180,y=220,width=TAM_BOTON , height=TAM_BOTON)

Button(root, text='0' , command=lambda:set_num(0)).place(x=40,y=280,width=190 , height=TAM_BOTON)


Button(root, text='+' , command=lambda:operation("+")).place(x=260,y=100,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='-' , command=lambda:operation("-")).place(x=260,y=160,width=TAM_BOTON , height=TAM_BOTON)
Button(root, text='*' , command=lambda:operation("*")).place(x=260,y=220,width=TAM_BOTON , height=TAM_BOTON)

Button(root, text='/' , command=lambda:operation("/")).place(x=330,y=100,width=TAM_BOTON , height=TAM_BOTON)

Button(root, text='Cls' , command=cls_method).place(x=330,y=160,width=TAM_BOTON , height=TAM_BOTON + 60)
Button(root, text='=' , command=igual).place(x=260,y=280,width=190 , height=TAM_BOTON)


root.mainloop()