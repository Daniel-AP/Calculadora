import math
from tkinter import  Button, Entry, Frame,  StringVar, Tk

#CREACION DE VARIABLES GLOBALES
Resultado = 0
Nums = ""
Ver = "-"
Textoeval = ""
EstadoOperacion = ""
#CREACION DE VENTANA
root = Tk()
root.iconbitmap("Fotos InterfacesGraficas\descarga.ico")
root.title("Calculadora")
root.config(bg="white")
root.geometry("355x450")
root.resizable(height=False,width=False)
#CREACION FRAME DE BOTONES
miFrame = Frame()
miFrame.config(bg="white")
miFrame.config(height=350,width=350)
miFrame.place(x=13,y=122)
#CREACION BOTONES Y FUNCIONES

##--------- BOTON COMANDO PI ---------
def PiComando(mensaje):
    global Nums, Ver, EstadoOperacion
    if Ver == "Igual":
        Progreso.delete(0,"end")
        operaciones.delete(0,"end")
        Ver = ""
    Num1 = operaciones.get()
    for i in Num1:
        if i == "-" or i == "√":
            EstadoOperacion = "SePuedePi"
    while ( ( (Ver != "*" or Ver != "/" or Ver != "-" or Ver != "+") and len(operaciones.get()) ) and EstadoOperacion != "SePuedePi" )> 0:
        mensaje = ""
        if mensaje == "":
            EstadoOperacion = ""
            break
    else:
        mensaje = "π"
    Num1 = operaciones.get()
    NumsLen = Num1 + mensaje
    TextoOperaciones.set(NumsLen)
    if len(TextoOperaciones.get()) > 0:
        TextoOperaciones.set(TextoOperaciones.get()[:22])
    Ver = "Numero"

#--------- BOTON COMANDO NEGATIVO ---------
def Negativo(mensaje):
    global Nums, Ver
    if Ver == "Igual":
        Progreso.delete(0,"end")
        operaciones.delete(0,"end")
        Ver = ""
    Num1 = operaciones.get()
    for i in Num1:
        while i == "-" or len(operaciones.get()) > 0:
            mensaje = ""
            if mensaje == "":
                break
        else:
            mensaje = "-"
    NumsLen = Num1 + mensaje
    TextoOperaciones.set(NumsLen)
    if len(TextoOperaciones.get()) > 0:
        TextoOperaciones.set(TextoOperaciones.get()[:22])
    Ver = "Numero"

#--------- BOTON COMANDO PUNTO DECIMAL ---------
def PuntoDecimal(mensaje):
    global Nums, Ver
    if Ver == "Igual":
        Progreso.delete(0,"end")
        operaciones.delete(0,"end")
        Ver = ""
    if len(operaciones.get()) <= 18:
        Num1 = operaciones.get()
        for i in Num1:
            while i == "." or i == "π":
                mensaje = ""
                if mensaje == "":
                    break
            else:
                mensaje = "."
            if Num1.find("inf") != -1:
                mensaje = ""
        NumsLen = Num1 + mensaje
        TextoOperaciones.set(NumsLen)
    Ver = "Numero"

#--------- BOTON C COMANDO  ---------
def CBotonComando():
    global Textoeval, Ver
    Textoeval = ""
    operaciones.delete(0,"end")
    Progreso.delete(0,"end")
    Ver = "C"

#--------- BOTON COMANDO RESULTADO ---------    
def PresentarResultadoComando(mensaje):
    operaciones.delete(0,"end")
    TextoOperaciones.set(mensaje)

#--------- BOTON COMANDO ---------   
def BotonComando(mensaje):
    global  Nums, Ver, EstadoOperacion

    if len(operaciones.get()) <= 18:
        EstadoOperacion = ""
        if Ver == "Igual":
            Progreso.delete(0,"end")
            operaciones.delete(0,"end")
            Ver = ""
        Nums = operaciones.get()
        NumsPantalla = ""
        for i in Nums:
            if i == "π":
                mensaje = ""
                if mensaje == "":
                    break
        if Nums.find("inf") != -1:
            mensaje = ""
        NumsPantalla = Nums + mensaje
        for i in NumsPantalla:
            if i == ".":
                Ver = "."
        if Ver != ".":
            for i in NumsPantalla:
                if i == "√":
                    NumsPantalla = NumsPantalla.replace("√","")
                    EstadoOperacion = "√"
            if len(NumsPantalla) > 3 and i != "√":
                if NumsPantalla.isdecimal:
                    NumsPantalla = NumsPantalla.replace(",","")
                    NumsPantalla = float(NumsPantalla)
                    NumsPantalla = "{:,}".format(NumsPantalla)
                else:
                    NumsPantalla = NumsPantalla.replace(",","")
                    NumsPantalla = int(NumsPantalla)
                    NumsPantalla = "{:,}".format(NumsPantalla)
            NumsPantalla = str(NumsPantalla)

            if NumsPantalla.endswith(".0"):
                suffix = ".0"
                NumsPantalla = NumsPantalla.removesuffix(suffix)
            if EstadoOperacion == "√":
                NumsPantalla = "√" + NumsPantalla
        TextoOperaciones.set(NumsPantalla)

    Ver = "Numero"       

#--------- BOTON COMANDO MULTIPLICACION ---------
def BotonComandoOperadoresX():
    global  TextoRecuento, Nums, Ver, Textoeval, EstadoOperacion
    
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ):
        TextoRecuento.set(Progreso.get() + Nums + "  ×  ")

    Ver = "*"
    operaciones.delete(0,"end")

#--------- BOTON COMANDO DIVISION ---------
def BotonComandoOperadoresDiv():
    global  TextoRecuento, Nums, Ver, Textoeval, EstadoOperacion
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ):
        TextoRecuento.set(Progreso.get() + Nums + "  ÷  ")
    
    Ver = "/"
    operaciones.delete(0,"end")

#--------- BOTON COMANDO MENOS ---------
def BotonComandoOperadoresMen():
    global  TextoRecuento, Nums, Ver, Textoeval, EstadoOperacion
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ):
        TextoRecuento.set(Progreso.get() + Nums + "  -  ")
   
    Ver = "-"
    operaciones.delete(0, "end")

#--------- BOTON COMANDO MAS ---------
def BotonComandoOperadoresMas():
    global  TextoRecuento, Nums, Ver, Textoeval, EstadoOperacion
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ): 
        TextoRecuento.set(Progreso.get() + Nums + "  +  ") 

    Ver = "+"
    operaciones.delete(0, "end")

#--------- BOTON COMANDO RAIZ CUADRADA ---------
def RCuadradaComando(mensaje):
    global  Nums, Ver
    if Ver == "Igual":
        Progreso.delete(0,"end")
        operaciones.delete(0,"end")
        Ver = ""
    Num1 = operaciones.get()
    for i in Num1:
        while i == "√" or len(operaciones.get()) > 0:
            mensaje = ""
            if mensaje == "":
                break
        else:
            mensaje = "√"
    NumsPantalla = Num1 + mensaje
    TextoOperaciones.set(NumsPantalla)
    if len(TextoOperaciones.get()) > 0:
        TextoOperaciones.set(TextoOperaciones.get()[:22])

#--------- BOTON COMANDO EXPONENTE ---------
def ExponenteComando():
    global  TextoRecuento, Nums, Ver, Textoeval
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ):
        TextoRecuento.set(Progreso.get() + Nums + "  ^  ")
    operaciones.delete(0,"end")
    Ver = "^"

#--------- BOTON COMANDO PORCENTAJE ---------
def BotonPorcentaje():
    global TextoRecuento,Nums, Ver, Textoeval
    if Ver == "Igual":
        Progreso.delete(0,"end")
    Nums = operaciones.get()
    if Ver == "Numero" or (Ver == "Igual" and len(operaciones.get()) != 0 ):
        TextoRecuento.set(Progreso.get() + Nums + "  %  ")
    operaciones.delete(0,"end")
    Ver = "%"

#--------- BOTON COMANDO IGUAL ---------
def BotonIgual():
    global Resultado, TextoRecuento, Ver, EstadoOperacion, Textoeval
    try:
        try:
            try:
                try:
                    if Ver == "Igual":
                        Progreso.delete(0,"end")
                        operaciones.delete(0,"end")
                    Ver = ""
                    for i in operaciones.get():
                        if i == "√":
                            EstadoOperacion = "SePuede"
                    if Progreso.get() != "" or EstadoOperacion == "SePuede":
                        TextoRecuento.set(Progreso.get() + operaciones.get() + " =  ")
                        Textoeval = Progreso.get()
                        Textoeval = Textoeval.replace("=","")
                        Textoeval = Textoeval.replace(" ","")
                        Textoeval = Textoeval.replace(",","")
                        
                        # MULTIPLICACION
                        Textoeval = Textoeval.replace("×","*")
                        # DIVISION
                        Textoeval = Textoeval.replace("÷","/")
                        
                        textoPreEval = Textoeval

                        # PORCENTAJE
                        pos = -1
                        pos = textoPreEval.find("%")
                        nuevaPreEval = textoPreEval
                        while pos != -1:
                            nuevaPreEval = textoPreEval.replace("%","/100*")
                            pos = nuevaPreEval.find("%",pos,len(nuevaPreEval))
                            textoPreEval = nuevaPreEval

                        # EXPONENTE
                        nuevaPreEval = nuevaPreEval.replace("^","**")
        
                        # PI
                        nuevaPreEval = nuevaPreEval.replace("π","3.1415926536")

                        # RAIZ CUADRADA
                        pos = -1
                        pos = nuevaPreEval.find("√")
                        while (pos != -1):  
                            subPreEval = nuevaPreEval[pos:len(nuevaPreEval)]
                            posfinal = len(subPreEval)
                            for i in subPreEval:
                                if i == "*" or i == "/" or i == "-" or i == "+":
                                    posfinal = subPreEval.find(i)
                                    break
                            subPreEval = nuevaPreEval[pos+1:pos+posfinal]
                            subPreEval2 = math.sqrt(eval(nuevaPreEval[pos+1:pos+posfinal]))
                            subPreEval2 = str(subPreEval2)

                            nuevaPreEval = nuevaPreEval.replace("√"+subPreEval,subPreEval2,1)
                            pos = nuevaPreEval.find("√")

                        #RESULTADO
                        
                        if nuevaPreEval.find("inf") != -1:
                            Resultado = "inf"
                        else:
                            try:
                                Resultado = (eval(nuevaPreEval))
                            except OverflowError:
                                Resultado = ""
                        #   FILTROS/EXTRAS
                        #--------------------------------------------------------
                        Resultado = str(Resultado)

                except NameError:
                    Resultado = ""
            except ValueError:
                Resultado = ""
        except TypeError:
            Resultado = ""
    except SyntaxError:
        Resultado = ""           
    if Resultado == "":
        PresentarResultadoComando(Resultado)
    if Resultado == "inf":
        PresentarResultadoComando(Resultado)
    try:
        try:
            if Resultado.isdecimal:
                Resultado = float(Resultado)
                Resultado = "{:,}".format(Resultado)
            else:
                Resultado = int(Resultado)
                Resultado = "{:,}".format(Resultado)
        except AttributeError:
            Resultado = ""
    except ValueError:
        Resultado = ""
    if Resultado == "":
        PresentarResultadoComando(Resultado)
    Resultado = str(Resultado)
    if Resultado.endswith(".0"):
        suffix = ".0"
        Resultado = Resultado.removesuffix(suffix)
    
    PresentarResultadoComando(Resultado)
        
    #  REINICIOS
    #--------------------------------------------------------
    
    Resultado = ""
    Ver = "Igual"
    EstadoOperacion = ""
    Textoeval = ""  
    textoPreEval = ""
    
    #--------------------------------------------------------            

#--------- BOTON COMANDO BORRAR ---------
def BotonComandoBorrar():
    global TextoOperaciones, EstadoOperacion, Ver
    EstadoOperacion = ""
    Borrar = operaciones.get()
    Borrar = Borrar[:-1]
    if Borrar.endswith("."):
        Borrar = Borrar.removesuffix(".")
    for i in Borrar:
        if i == ".":
            Ver = "."
    if Ver != ".":
        for i in Borrar:
            if i == "√":
                Borrar = Borrar.replace("√","")
                EstadoOperacion = "√"
        if len(Borrar) > 3 and i != "√":
            if Borrar.isdecimal:
                Borrar = Borrar.replace(",","")
                Borrar = float(Borrar)
                Borrar = "{:,}".format(Borrar)
            else:
                Borrar = Borrar.replace(",","")
                Borrar = int(Borrar)
                Borrar = "{:,}".format(Borrar)
        Borrar = str(Borrar)

        if Borrar.endswith(".0"):
            suffix = ".0"
            Borrar = Borrar.removesuffix(suffix)
        if EstadoOperacion == "√":
            Borrar = "√" + Borrar
            EstadoOperacion = ""
    TextoOperaciones.set(Borrar)
    Ver = "B"

#TEXTVARIABLEs
TextoOperaciones = StringVar()
TextoRecuento = StringVar()


c = Button(miFrame,text="C",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command= CBotonComando)
c.grid(row=0,column=1,padx=1,pady=1)

delNums = Button(miFrame,text="\u232B",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command= BotonComandoBorrar)
delNums.grid(row=0,column=2,padx=1,pady=1)

porcentaje = Button(miFrame,text="%",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command= BotonPorcentaje)
porcentaje.grid(row=5,column=0,padx=1,pady=1)

uno1 = Button(miFrame,text=1,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("1"))
uno1.grid(row=1,column=0,padx=1,pady=1)

dos2 = Button(miFrame,text=2,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("2"))
dos2.grid(row=1,column=1,padx=1,pady=1)

tres3 = Button(miFrame,text=3,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("3"))
tres3.grid(row=1,column=2,padx=1,pady=1)

cuatro4 = Button(miFrame,text=4,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("4"))
cuatro4.grid(row=2,column=0,padx=1,pady=1)

cinco5 = Button(miFrame,text=5,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("5"))
cinco5.grid(row=2,column=1,padx=1,pady=1)

seis6 = Button(miFrame,text=6,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("6"))
seis6.grid(row=2,column=2,padx=1,pady=1)

siete7 = Button(miFrame,text=7,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("7"))
siete7.grid(row=3,column=0,padx=1,pady=1)

ocho8 = Button(miFrame,text=8,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("8"))
ocho8.grid(row=3,column=1,padx=1,pady=1)

nueve9 = Button(miFrame,text=9,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("9"))
nueve9.grid(row=3,column=2,padx=1,pady=1)

menos_numero = Button(miFrame,text="+/-",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:Negativo("-"))
menos_numero.grid(row=4,column=0,padx=1,pady=1)

cero0 = Button(miFrame,text=0,font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:BotonComando("0"))
cero0.grid(row=4,column=1,padx=1,pady=1)

punto = Button(miFrame,text=".",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dodger blue",command= lambda:PuntoDecimal("."))
punto.grid(row=4,column=2,padx=1,pady=1)

dividir = Button(miFrame,text="÷",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command=BotonComandoOperadoresDiv)
dividir.grid(row=0,column=3,padx=1,pady=1)

Mult = Button(miFrame,text="×",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command=BotonComandoOperadoresX)
Mult.grid(row=1,column=3,padx=1,pady=1)

menos = Button(miFrame,text="-",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command=BotonComandoOperadoresMen)
menos.grid(row=2,column=3,padx=1,pady=1)

mas = Button(miFrame,text="+",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command=BotonComandoOperadoresMas)
mas.grid(row=3,column=3,padx=1,pady=1)

igual = Button(miFrame,text="=",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command=BotonIgual)
igual.grid(row=4,column=3,padx=1,pady=1)

off = Button(miFrame,text="◯",font=("arial",13,"bold"),bg="red",width=7,height=2,fg="white",command=root.destroy)
off.grid(row=0,column=0,padx=1,pady=1)

Pi = Button(miFrame,text="π",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange",command= lambda:PiComando("π"))
Pi.grid(row=5,column=1,padx=1,pady=1)

RCuadrada = Button(miFrame,text="√",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange", command = lambda:RCuadradaComando("√"))
RCuadrada.grid(row=5,column=2,padx=1,pady=1)

Exponente = Button(miFrame,text="X^",font=("arial",13,"bold"),bg="white",width=7,height=2,fg="dark orange", command= ExponenteComando )
Exponente.grid(row=5,column=3,padx=1,pady=1)

#--------- FRAMES Y ENTRYs ---------
miFrame2 = Frame(root)
miFrame2.config(height=110,width=350)
miFrame2.config(bg="red")   
miFrame2.place(x=0,y=13)

operaciones = Entry(miFrame2,textvariable=TextoOperaciones,font=("arial",20),fg="black",justify="right")
operaciones.config(bg="white")
operaciones.place(x=0,y=0,width=350,height=110)

Progreso = Entry(miFrame2,textvariable=TextoRecuento,font=("arial",10),fg="grey",justify="right")
Progreso.config(bg="white")
Progreso.place(x=0,y=0,width=350,height=25)

root.mainloop()