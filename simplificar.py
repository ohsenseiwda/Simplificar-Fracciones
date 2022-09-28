from tkinter import *
#Esta app es un proyecto para simplificar fracciones.
#Muy simple y facil de usar.
def simplificar():
#Almaceno las variables del que vienen -cuadroTexto1 y -cuadroTexto2 en -aux1 y -aux2 para luego con el condicional -IF verificar si el valor ingresado por el usuario es de valor NUMERICO o ALFANUMERICO.
	aux1=cuadroTexto1.get()
	aux2=cuadroTexto2.get()
#La variable -va incrementa su valor mas adelante
	va=2
#Aqui este -IF verifica que los valores sean digitos para asi realizar los calculos, de no ser digitos, la funcion devuelve nada, creo. jeje.
	if aux1.isdigit() and aux2.isdigit():
#Aqui se convierten las variables digitales en un valor entero -INT.
		num1=int(aux1)
		num2=int(aux2)
#Este bucle -FOR se repite 101 veces, incrementando el valor de -va en 1 por cada vuelta.
		for i in range(1,100):
#Esta parte es dificil de explicar, pero basicamente esta parte es para comprobar si el valor luego de dividirlo y multiplicarlo da como resultado el numero inicial, o con decimales.
			valorA1=int(num1/va)
			valor1=valorA1*va
			valorA2 =int(num2/va)
			valor2=valorA2*va
#Este -IF comprueba que el valor es divisible sin que de como resultado un numero con decimales.
			if valor1 == num1 and valor2 == num2 and valor1 != 0 and valor2 != 0:
				num1=int(num1/va)
				num2=int(num2/va)
#Si el valor da como resultado un valor incorrecto, se lanza este -ELSE.
			else:
#Aqui el -va aumenta su valor original en 1
				va=va+1
#este -IF sirve para mostar cuando la fraccion da como resultado un valor con denominador 1 mostrando solo el numerador.
		if num2 == 1:
			resultado=str(num1)
#Este -ELSE muestra el resultado en caso de no cumplirse la condicion anterior.
		else:
			resultado=str(num1)+"/"+str(num2)
		return var.set(resultado)

#Desde aca en adelante ya no explicare porque me da pereza jajaj
raiz=Tk()
raiz.title("Simplificar Fracciones")
raiz.config(bg="#32081D")
var=IntVar()

miFrame=Frame(raiz)
miFrame.pack(padx=50,pady=500)
miFrame.config(bg="#003D52")
#Por si acaso prueban este codigo en PC y no se ve correctamente, quitar el '#'' de la siguente linea.
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