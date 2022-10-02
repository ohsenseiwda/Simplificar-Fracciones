from tkinter import *

def simplificar():
	aux1=cuadroTexto1.get()
	aux2=cuadroTexto2.get()
	x=2
	if aux1.isdigit() and aux2.isdigit():
		num1=int(aux1)
		num2=int(aux2)
		for i in range(1,1000):
			valor1=num1%x
			valor2=num2%x
			if valor1 == 0 and valor2 == 0:
				num1=int(num1/x)
				num2=int(num2/x)
			else:
				x=x+1
		if num2 == 1:
			resultado=str(num1)
		else:
			resultado=str(num1)+"/"+str(num2)
		return var.set(resultado)

raiz=Tk()
raiz.title("Simplificar Fracciones")
raiz.config(bg="#32081D")
var=IntVar()

miFrame=Frame(raiz)
miFrame.pack(padx=50,pady=500)
miFrame.config(bg="#003D52")
#miFrame.config(width="720",height="720")
miFrame.config(bd="15")
miFrame.config(relief="groove")

miTitulo=Label(miFrame,text="Simplificador de fracciones",font=("",10),bg="#003D52",fg="white")
miTitulo.grid(row=0,column=0,columnspan=2,padx=150,pady=25)

miNumerador=Label(miFrame,text="NUMERADOR",font=("",6),bg="#003D52",fg="white")
miNumerador.grid(row=1,column=0)

miDenominador=Label(miFrame,text="DENOMINADOR",font=("",6),bg="#003D52",fg="white")
miDenominador.grid(row=2,column=0)

cuadroTexto1=Entry(miFrame)
cuadroTexto1.grid(row=1,column=1,padx=25,pady=25)
cuadroTexto1.config(justify="center")

cuadroTexto2=Entry(miFrame)
cuadroTexto2.grid(row=2,column=1,padx=25,pady=25)
cuadroTexto2.config(justify="center")

botonEnvio=Button(miFrame,text="Resultado",command=simplificar)
botonEnvio.grid(row=3,column=0,columnspan=2,pady=50)

res=Label(miFrame,textvariable=var,font=("",16),bg="#003D52",fg="green")
res.grid(row=4,column=0,columnspan=2,pady=25)

raiz.mainloop()