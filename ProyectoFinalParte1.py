"""
Este programa simular el agente autono de una cafetera programable la cual debera 
cumplir con ciertas condiciones para que el producto salga como veremos a continuacion
esperando que sea una base para futuros estudios y para la construccion propia de un 
agente autonomo

Autores:
José SanMartín

Versión:
VER 1.0
"""
#Importamos las bibliotecas necesarias
import time, os
#Creamos una variable para sumar los costos 
costo=0
#Creamos una variable para llevar la cantidad de cacao
cacao=20
#Creamos una variable para llevar la cantidad de Leche en polvo
leche_en_polvo=20
#Creamos una variable para llevar la cantidad de Cafe
cafe=20
#Creamos una variable para llevar la cantidad de Agua
agua=1000
#Creamos una variable para llevar la cantidad de Agua caliente
aguacaliente=0
#Creamos un cojunto para las horas 
horas=[]
#Creamos una lista para el sabor 
sabor=[]
def actuarSolo():
    """
    Es una funcion la cual efectuara la accion del agente autonomo de realizar una 
    accion previamente programada 
    Recibe
    ------------
       No recibe ningun parametro
    Retorna:
    ------------
       moca(): Funcion que nos envia a realizar esta accion 
       chocolatada(): Funcion que nos envia a realizar esta accion 
       expresso(): Funcion que nos envia a realizar esta accion 
    """
    #Llamamos a a la variable global costo
    global costo
    #Al actuar solo el costo aumenta en 1
    costo+=1
    #El lmimte de caracteres que tomara una variables 
    limite=5 
    #Mientras la opcion sea falsa    
    while True:
        #Creamos un restriccion
        try:
            #Permitimos la usuario ingresar una hora en formato de HH:MM 
            hora=(input("Por favor ingresar un hora en formar de [HH:MM] : ")[:limite])
            #En caso de que no sea posible 
        except ValueError:
            #Imprimir mensaje de advertencia 
            print("Deber ser un numero")
            #Continuar
            continue 
        #revisamos que el horario se encuentre en la lista de horaraios     
        if hora in horas:
            #Recorremos la lista 
            for x in sabor:
                #Revisamos cual es la opcion que concuerda con la lista
                if x == "1":
                    #Regresamos a la opcion deseada
                    return chocolatada()
                #Revisamos cual es la opcion que concuerda con la lista
                elif x == "2":
                    #Regresamos a la opcion deseada
                    return moca()
                    #Revisamos cual es la opcion que concuerda con la lista
                elif x == "3":
                    #Regresamos a la opcion deseada
                    return expresso()
        #En caso de que no cumpla ninguno
        else:
            #Enviamos mensaje
            print("No existe acciones programadas")
            #Esperamos 
            os.system("pause")
            #Regresamos al menu
            menu()
def programar():
    """
    Es una funcion la recibira algunos parametros para poder nosotros programar la accion automatica del
    agente autonmo enviando esta a sus funciones correspondientes 
    Recibe
    ------------
       No recibe parametros 
           
    Retorna:
    ------------
       programarhora(): Esta funcion nos permite seguir con el proceso de programacion automatica 
    """
    #Creamos la variable globar 
    global costo
    #Ingresamos una opcion para que el usaurio seleccion el valor que desea 
    sabore=input("Ingrese el sabor que desea programar: \n1.-Chocolatada \n2.-Mocachinno \n3.-Cafe Expresso \nOpcion: ")
    #Validamos que ingresemos solo opciones validas 
    while sabore != "0":
        #Creamos un opcion para un sabor 
        if sabore == "1":
            #Imprimmos mensaje
            print("Sabor Elegido: Chocolatada")
            #Enviamos orden al cojunto correspondiente
            sabor.append(sabore)
        #Si se elige la opcion
        elif sabore == "2":
            #Imprimos Mensaje 
            print("Sabor Elegido Mocachino")
            #Enviamos orden al cojunto correspondiente
            sabor.append(sabore)
            #Si se elige la opcion
        elif sabore == "3":
            #Imprimos Mensaje
            print("Sabor Elegido: Cafe")
            #Enviamos orden al cojunto correspondiente
            sabor.append(sabore)
        #Caso contrario
        else:
            #Imprimos mensaje
            print("Opcion incorrecta Digite una valida")
            #Volvemos a Programar
            return programar()
            #Se rompe el bucle
        break
    #Programos hora 
    costo+=1
    programarhora()
def programarhora():
    """
    Es una funcion que  nos permite seguir con el proceso de programacion automatica pues aqui
    programaremos las horas 
    Recibe
    ------------
       No recibe ningun parametro
           
    Retorna:
    ------------
       menu(): nos regresa al menú principal
    """
    #Creamos la variable globar 
    global costo
    #Declaramos un limite
    limite=5    
    while True:#Se inicia un bucle
        try:#Caputramos excpeciones 
            #ingresamos la hora 
            hora=(input("Por favor ingresar un hora en formar de [HH:MM] : ")[:limite])
            #Captura de Errores
        except ValueError:
            #Imprimir menasje 
            print("Deber ser un numero")
            #Se continua 
            continue 
        #Se toma las primeras partes de la variable 
        H=int(hora[0:2])
        #Se separa la variable
        M=int(hora[3:5])
        #Validamos que los datos ingresado sean correctos 
        if H<0 or H>23:
            #imprimos mensaje de advertencia
            print("La hora no puede ser menor a 0 ni mayor a 23")
            #Regresamos a la opcion correca 
            return programarhora()
        #Validamos que los mintuos sean correctos
        if M<0 or M>59:
            #Mensaje de advertencia
            print("Los minutos no puede ser menor a 0 ni mayor a 59")
            #Regresamos a la opcion correca 
            return programarhora()
        #Caso contrario
        else:
            #Sale del bucle
            break
    #Aumentamos el costo
    costo+=1
    #Agregamos la hora al conjunto
    horas.append(hora)
    #Comprabammos que se guarde la informaicon
    print(horas,sabor)
    #Volvemos a lmenu principal
    menu()
def sensor():
    """
    Es una funcion la cual activara nuestro "sensor" para ver si es factible 
    continuar con las acciones 
    Parametros:
    Recibe
    ------------
       No Recibe Parametros 
           
    Retorna:
    ------------
       expenderagua(): Es el sigueinte paso una vez hayamos validado el sensor
    """
    #Llammos la vairabel global
    global costo,aguacaliente
    #Creamos una opcion recipinete
    recipiente=input("Esta una taza o recpiente ubicado? si(1) o 2(no)")
    #Validamos lo que pasa si el numero es 1
    if recipiente == "1":
        #Regresamos a la funcion correcta 
        expenderagua()
        #Aumenta el costo
        costo +=1
     #Validamos lo que pasa si el numero es 2
    elif recipiente=="2":
        #imprimos una mensaje 
        print("entrando a modo reposo... Esperando a que se coloque un recipiente ")
        #Espermaos salir del modo reposo
        os.system("Pause")
        #Aumenta el costo por salir de modo repsoso
        costo+=1
        aguacaliente+=150
        #Enviamos mensaje
        print("Volviendo a Encender")
        #Simulamos que se enciende
        time.sleep(2)
        #Vamos a la función necesaria 
        sensor()
    #Caso contrario
    else:
        #Se envia mensaje 
        print("opcion no valida")
        #No aumenta costo
        costo+=0
        #Enviamos a la opcion correcta 
        sensor()
def expenderagua():
    """
    Es una funcion la cual realizar la funcion de dar agua a nuestro prodcuto para 
    que este pueda ser elaborado
    Recibe 
    ------------
       No Recibe parametro
           
    Retorna:
    ------------
       recargar() si es necesario nos devolvera a esa funcion para poder recagar agua
    """
    #Llamamos a las variables globales 
    global agua, aguacaliente,costo
    #Creamos un condicion en caso de que no exita agua calietne almacenada
    if aguacaliente==0 and agua>0:
        #Expendemos una cierta cantidad de agua 
        agua-=150
        #Simulamos la accion realizada
        print("Calentando Agua")
        #Agregamos el agua caliente al agua retirada
        aguacaliente+=150
        #Aumenta el costo en 1
        costo+=1
    #Si el agua caliente es 0
    elif aguacaliente>0:
        #Se resta el agua caliente
        aguacaliente-=150
        #No suma el costo
        costo+=0
    elif aguacaliente==0 and agua<150:
        #Imprimir mensaje
        print("Por favor recargue agua")
        #Regresamos a la opcion correcta
        return recargar()  
def recargar():
    """
    Es una funcion la cual nos permitira recargar si es necesario alguna materia prima 
    tomando en cuenta que esta no puede exceder cierta cantidad 
    Recibe
    ------------
       No recibe parametros 
           
    Retorna:
    ------------
       menu(): Nos devuelve al menu cuando ya no veamos necesario seguir usando la función
    """
    #llamamos las variables locales
    global costo,cacao,leche_en_polvo,cafe,agua
    #Ingressar el material que deseamos recargar
    materia=input("Seleccione el producto que desea realizar:\n1.-Cacao \n2.-Leche en Polvo \n3.-Cafe \n4.-Agua \n0-Menu \nInserte Opcion:  ")
    #Iniciamos un bucle que nos deje ingresar una opción correcta 
    while materia !="@":
        #Creamos una opcion por si se elige recargar cacao
        if materia =="1":
            while True:
        #Creamos la condicion para validar datos 
                try:
                #Creamos una funcion que nos permita ingresar la variable dato
                    recarga=int(input("Ingrese el valor a recargar: "))
                    #Revisamos que la condicion se cumpla 
                except ValueError:
                    #Enviamos un mensaje de advertencia
                    print("Debe ser un numero")
                    #Continuamos si las condiciones se cumplen
                    continue
                #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
                if recarga<=0:
                    #Evaimos un mensaje de advertencia 
                    print("Debe ser un numero positivo y diferente de 0")
                    #Se crea la condicion para salir del bucle 
                if recarga>1000 and cacao<1000:
                    #Evaimos un mensaje de advertencia 
                    print("No puede exceder la capacidad del tanque")
                    recarga1 = 1000-cacao
                    cacao+=recarga1
                    return recargar()
                    #Se crea la condicion para salir del bucle 
                else:
                    #Salimos del bucle
                    break
            #Agregamos la cantidad de cacao recagarda
            cacao+=recarga           
            
            #Imprimimos el valor del cacao
            print("la cantidad actual de cacao es: ",cacao)
            #retornamos al menu principal
            print("regresando a menu principal")
            #Regramos al menu principal
            recargar()
        #Creamos una opcion por si se elige recargar leche en polvo
        if materia =="2":
            #Creamos un bucle para validar que los datos sean correctas
            while True:
        #Creamos la condicion para validar datos 
                try:
                #Creamos una funcion que nos permita ingresar la variable dato
                    recarga=int(input("Ingrese el valor a recargar: "))
                    #Revisamos que la condicion se cumpla 
                except ValueError:
                    #Enviamos un mensaje de advertencia
                    print("Debe ser un numero")
                    #Continuamos si las condiciones se cumplen
                    continue
                #Creamos otra condicion en la cual el dato debe ser un nunmero positivo
                if recarga<=0:
                    #Evaimos un mensaje de advertencia 
                    print("Debe ser un numero positivo y diferente de 0")                    
                #No puede exceder el alamacenamiento 
                if recarga>1000 and leche_en_polvo<1000:
                    #Evaimos un mensaje de advertencia 
                    print("No puede exceder la capacidad del tanque")
                    recarga1 = 1000-leche_en_polvo
                    leche_en_polvo+=recarga1
                    return recargar() 
                    #condicion para salir del bucle 
                else:
                    #Salimos del bucle
                    break
            #Aumentamos al recarga en el valor de cafe
            
            #Aumentamos el costo
            costo+=1
            #Imprimimos el valor del cafe 
            print("La cantidad  acutal de Leche en polvo es: ",leche_en_polvo)
            #Regresamos al menu principal
            print("regresando a menu principal")
            #Se retorna al menu principal
            recargar()
        #Creamos una opcion por si se elige recargar cacao
        if materia =="3":
            #Creamos un bucle para validar que los datos sean correctas
            while True:
        #Creamos la condicion para validar datos 
                try:
                #Creamos una funcion que nos permita ingresar la variable dato
                    recarga=int(input("Ingrese el valor a recargar: "))
                    #Revisamos que la condicion se cumpla 
                except ValueError:
                    #Enviamos un mensaje de advertencia
                    print("Debe ser un numero")
                    #Continuamos si las condiciones se cumplen
                    continue
                #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
                if recarga<=0:
                    #Evaimos un mensaje de advertencia 
                    print("Debe ser un numero positivo y diferente de 0")
                if recarga>1000 and cafe<1000:
                    #Evaimos un mensaje de advertencia 
                    print("No puede exceder la capacidad del tanque")
                    recarga1 = 1000-cafe
                    cafe+=recarga1
                    return recargar()
                #Se crea la condicion para salir del bucle 
                else:
                    #Salimos del bucle
                    break
            #Aumentamos al valor de la leche en polvo el valor de la recarga
            cafe+=recarga
            #Aumentamos el costo
            
            #Imprimir la cantidad actual de leche en polvo 
            print("La cantidad acutal de cafe es: ",cafe)
            #Mensaje de regreso ak menu principal
            print("regresando a menu principal")
            #Volver al menu principal
            recargar()
        if materia =="4":
            #Condicion para validar datos 
            while True:
        #Creamos la condicion para validar datos 
                try:
                #Creamos una funcion que nos permita ingresar la variable dato
                    recarga=int(input("Ingrese el valor a recargar: "))
                    #Revisamos que la condicion se cumpla 
                except ValueError:
                    #Enviamos un mensaje de advertencia
                    print("Debe ser un numero")
                    #Continuamos si las condiciones se cumplen
                    continue
                #Creamos otra condicion en la cual el radio debe ser un nunmero positivo
                if recarga<=0:
                    #Evaimos un mensaje de advertencia 
                    print("Debe ser un numero positivo y diferente de 0")
                    #Se crea la condicion para salir del bucle 
                if recarga>1500 and agua<1500:
                    #Evaimos un mensaje de advertencia 
                    print("No puede exceder la capacidad del tanque")
                    recarga1 = 1500-agua
                    agua+=recarga1
                    return recargar()
        #Aumentamos le valor de la recarga 
        agua+=recarga
        #Agreamos un costo a esta accion        
        #El valor acru
        print("La cantidad acutal de Agua es: ",agua)
        #Imprimimos un mensaje que regresas al menu principal
        print("regresando a menu principal")
        #Volvemos al menu principal
        recargar()
        if materia =="0":
            #Condicion para validar datos  
            return menu()
                #Se crea la condicion para salir del bucle 
        else:
            #Salimos del bucle
            break    
def chocolatada():
    """
    Es una funcion la cual realizara una taza de chocolatada tomando en cuenta ciertos parametros 
    y avisandonos en caso de que falte materia prima 
    Recibe
    ------------
       sensor(): Inicia nuetra funcion sensor
           
    Retorna:
    ------------
       recargar(): Nos devuelve a la opcion de recargar de faltar material
       menu(): Nos devuelve al menu tras realizar su trabajo o al querer cambiar de opinion
       
    """
    global costo,cacao,leche_en_polvo,cafe,agua
    #Imprimos el producto que estamos realizando
    print("realizando una chocolatada") 
    #Activamos el sensor antes que se realize la accion
             
    #Retiramos la cantidad adecuada de producto
    cacao -= 25
    #Retiramos la cantidad adecuada de producto
    leche_en_polvo -=25       
    if cacao < 25 or leche_en_polvo <25 or (agua <50 and aguacaliente<50):
        print("No existe el suficiente producto, por recargue mas o seleccione otro")
        #Anula la salida de cacaco
        cacao +=25
        #Anula la salida de leche en polvo
        leche_en_polvo +=25
        #Anula la salida de Agua
        agua +=50
        #Aumenta el costo
        costo+=1
        #creamos una opcion para que el usuario pueda recargar 
        ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
        #creamos un bucle que no nos deje ingresar una opciion incorrecta
        while ir_a_recargar!="0":
            #Creamos la opcion si se elige la primera opcion
            if ir_a_recargar == "1":
                #Retornamos al funcion que buscamos
                return recargar()
                #Caso contrario
            if ir_a_recargar == "2":
                return menu()
            else:
                #Se imrpime un mensaje de advertencia 
                print("Opcion no valida")
                #No saldra del bucle hasta que se elija una opcion correcta 
                ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
            break
    #Simulamos el tiempo de servido
    sensor()  
    print("Siviendo Chocolatada")
    time.sleep(2)
    print("Servidoo")
        #Agregamos costo
    costo += 1
        #Imrpimos el costo de la accion    
    print("el costo es: ",costo)  
        #volvemos al menu principal
    costo-=costo
    
    menu()
def moca():
    """
    Es una funcion la cual realizara una taza de Mocaccino tomando en cuenta ciertos parametros 
    y avisandonos en caso de que falte materia prima 
    Recibe
    ------------
       sensor(): Inicia nuetra funcion sensor
           
    Retorna:
    ------------
       recargar(): Nos devuelve a la opcion de recargar de faltar material
       menu(): Nos devuelve al menu tras realizar su trabajo o al querer cambiar de opinion
       
    """
    global costo,cacao,leche_en_polvo,cafe,agua
    #Imprimos el producto que estamos realizando
    print("realizando un Mocachinno")    
    sensor()        
    #Retiramos la cantidad adecuada de producto
    cacao -= 25
        #Retiramos la cantidad adecuada de producto
    leche_en_polvo -=25
        #Retiramos la cantidad adecuada de producto
    cafe-=25
    if cacao < 25 or leche_en_polvo <25 or agua <100 or cafe<25:
        print("No existe el suficiente producto, por recargue mas o seleccione otro")
        #Anula la salida de cacaco
        cacao +=25
        #Anula la salida de leche en polvo
        leche_en_polvo +=25
        #Anula la salida de Agua
        agua +=100
        #Anula la salida de Cafe
        cafe +=25
        #Aumenta el costo
        costo+=1
        #creamos una opcion para que el usuario pueda recargar 
        ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
        #creamos un bucle que no nos deje ingresar una opciion incorrecta
        while ir_a_recargar!="0":
            #Creamos la opcion si se elige la primera opcion
            if ir_a_recargar == "1":
                #Retornamos al funcion que buscamos
                return recargar()
                #Caso contrario
            if ir_a_recargar == "2":
                return menu()
            else:
                #Se imrpime un mensaje de advertencia 
                print("Opcion no valida")
                #No saldra del bucle hasta que se elija una opcion correcta 
                ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
            break
    #Simulamos el tiempo de servido
    print("Sirviendo Mocachinno")
    time.sleep(2)
    print("Servido")
        #Agregamos costo
    costo += 1
        #Imrpimos el costo de la accion    
    print("el costo es: ",costo)  
        #REiniciamos Costo
    costo-=costo    
    #Volver al menu
    menu()
def expresso():
    """
    Es una funcion la cual realizara una taza de Expresso tomando en cuenta ciertos parametros 
    y avisandonos en caso de que falte materia prima 
    Recibe
    ------------
       sensor(): Inicia nuetra funcion sensor
           
    Retorna:
    ------------
       recargar(): Nos devuelve a la opcion de recargar de faltar material
       menu(): Nos devuelve al menu tras realizar su trabajo o al querer cambiar de opinion
       
    """
    global costo,cacao,leche_en_polvo,cafe,agua
    #Imprimos el producto que estamos realizando
    print("Opcion Elegida expresso")       
    sensor()     
    #Retiramos la cantidad adecuada de producto
    cafe -= 25              
    
    if cafe < 25  or agua <50:
        print("No existe el suficiente producto, por recargue mas o seleccione otro")
        #Anula la salida de cacaco
        cafe +=25
        #Anula la salida de leche en polvo               
        agua +=50
        #aumneta costo
        costo+=1
        #creamos una opcion para que el usuario pueda recargar 
        ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
        #creamos un bucle que no nos deje ingresar una opciion incorrecta
        while ir_a_recargar!="0":
            #Creamos la opcion si se elige la primera opcion
            if ir_a_recargar == "1":
                #Retornamos al funcion que buscamos
                return recargar()
                #Caso contrario
            if ir_a_recargar == "2":
                return menu()
            else:
                #Se imrpime un mensaje de advertencia 
                print("Opcion no valida")
                #No saldra del bucle hasta que se elija una opcion correcta 
                ir_a_recargar=input("Desea recargar mas producto si(1) o no(2): ")
            break
    #Simulamos el tiempo de servido
    print("Sirviendo Expresso")
    time.sleep(2)
    print("Servido")
        #Agregamos costo
    costo += 1
        #Imrpimos el costo de la accion    
    print("el costo es: ",costo)    
        #volvemos al menu principal
    costo-=costo    
    menu()                    
def relizandoBebida():
    """
    Es una funcion la cual realizara una taza de la bebida elegida tomando en cuenta ciertos parametros 
    y avisandonos en caso de que falte materia prima 
    Recibe
    ------------
       opcion: es una variable la cual determinara el tipo de cafe a realizar
           
    Retorna:
    ------------
       chocolatada(): Realiza una chocolatada
       moca(): Realiza un Moca
       expresso(): Realiza un Expresso
       
    """
    #llamamos las variables locales
    global costo,cacao,leche_en_polvo,cafe,agua
   #Pedidos la opcion que se desea realizar
    opcion=input("Seleccione el producto que desea realizar:\n1.-Chocolatada \n2.-Mochacchino \n3.-Expresso \nInserte Opcion:  ")
   #Creamos una opción que nos no deje ingresar resultado erroneos
    while opcion !="0":
        #Si la opcion es igual a 1
        if opcion =="1":
            # Se aumenta el costo
            costo+=1
            #Retornamos a la opcion
            return chocolatada()            
        #Si la pcion es igual a 2                
        if opcion =="2":
            #Se aumenta el costo
            costo+=1
            #Retornamos a la opcion
            return moca()
        #Si la opciones e igual a 3
        if opcion =="3":
            #El costo aumenta en 1
            costo+=1
            #Regresamos a la opcion elegida
            return expresso()
            #Caso contrario
        else:
            #Imprimi mensaje de advertencia
            print("opcion no valida")
            #Volver a ingresa opcion
            opcion=input("Seleccione el producto que desea realizar:\n1.-Chocolatada \n2.-Mochacchino \n3.-Expresso \nInserte Opcion:  ")
def menu():
    """
    Es una funcion la recibira las funciones principales anteriores para poder llamarlas de una manera más 
    rapida  
    Parametros:
    ------------
       accion: es la variable la cual determinara cual de todas las funciones vamos a llamar 
           
    Retorna:
    ------------
       recargar(): Opcion para recargar materia prima 
       relizandoBebida(): Opcion para servir una bebida 
       programar(): Funcion para programar sistema autonomo
       actuarSolo(): Función para que actue solo el agente inteligente
    """
    #El usuario elige que accion realizar 
    accion=input("Ingrese la accion que desea realizar: \n1.-RECARGAR PRODUCTOS \n2.-REALIZAR BEBIDA \n3.-AUTOMATICO \n4.-INFO \n0.-SALIR \nSeleccion: ")
    #Mientras la accion sea diferente de 0 Entonces 
    while accion !="0":
        #Si la accion es igual a 1
        if accion == "1":
            #Regresamos a la opcion correcta 
            return recargar()
        #Si la accion es igual a 2
        elif accion == "2":
        #Regresamos a la opcion correcta 
            return relizandoBebida()
            #Si la accion es igual a 3
        elif accion =="3":
            #Regresamos a la opcion correcta 
            return programar()
        #Si la accion es igual a 4
        elif accion =="4":
            #Regresamos a la opcion correcta 
            print("Cantidad de Agua en la Maquina",agua)
            print("Cantidad de Agua Caliente en la Maquina",aguacaliente)
            print("Cantidad de Cacao en la Maquina",cacao)
            print("Cantidad de Leche en Polvo en la Maquina",leche_en_polvo)
            print("Cantidad de Cafe en la Maquina",cafe)
            os.system("Pause")
            menu()            
        elif accion =="5":
            #Regresamos a la opcion correcta 
            return actuarSolo()
        #Si no se da niguna de las opciones entonces 
        else:
            print("opcion no valida")
            #Regreamos a legir accion 
            accion=input("Ingrese la accion que desea realizar: ")

if __name__ == '__main__':
    #Damos un mensaje de bienvenida
    print("##############  CAFETERA  #############")
    #Llamamos al menu principal
    menu()

