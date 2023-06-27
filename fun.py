def menu():
    listaMenu=["Agregar auto","Mostrar auto","Modificar precio de venta y/o kilometraje","Vender Auto ","Salir"]
    for x in range(len(listaMenu)):
        print(f"{x+1}){listaMenu[x]}")
        
def op1(listapatente,listaprop,listaruts,listatelefono,listacorreo,listayir,listacarga,listapuertas,listatrm,listacolor,listakm,listaprecio,listamarca,listamodelo):
    while True:#nombre
        try:
            
            nombrepropietario=input("ingrese el nombre del propietario: ")
            
            validacion=validarletras(nombrepropietario)
            if validacion==True:
                listaprop.append(nombrepropietario)
                break
            else:
                print("ingresa un nombre valido")
            
            
        except:
            print("ingrese un nombre valido")
    while True:#rut
        try:
            rut=int(input("ingresa el rut: "))
            if rut>5000000 and rut<21000000:
                listaruts.append(rut)
                break
            else:
                print("ingrese un rut valido")
        except:
            print("ingrese un valor numerico")
    while True:#telefono
        try:
            telefono=int(input("ingrese el numero de telefono: "))
            telefono=str(telefono)
            if len(telefono)==9:
                listatelefono.append(telefono)
                break
            else:
                print("ingrese un numero valido")
        except:
            print("ingrese un valor numerico")
    while True:#correo
        try:
            correo=input("ingrese el correo: ")
            valcorreo=validarcorreo(correo)
            if valcorreo==True:
                listacorreo.append(correo)
                break
            else:
                print("error")
            
        except:
            print("ingrese un correo valido ")
            
    while True:
        try:
            auto=input("ingrese nombre vehiculo: ")
            listamodelo.append(auto)
            break
        except:
            print("error")
    while True:
        try:
            marca=input("ingrese marca vehiculo: ")
            listamarca.append(marca)
            break
        except:
            print("error")
    while True:
        try:
            patente=input("ingrese la patente: ")
            if len(patente)==6:
                valpat=validarpatente(patente,listapatente)
                if valpat==True:
                    print("patente no valida")    
                else:
                    listapatente.append(patente)
                    print(listapatente)
                    break
                
            else:
                print("ERROR")
            
        except:
            print("ingrese una patente valida")
    while True:
        try:
            yir=int(input("ingrese el año del vehiculo: "))
            if yir>=1900 and yir<=2024:
                listayir.append(yir)
                break
            else:
                print("ingrese un año valido")
        except:
            print("ingrese un año valido")
    while True:
        try:
            carga=input("ingrese si es diesel o kerosene: ")
            if carga=="diesel" or carga=="kerosene":
                listacarga.append(carga)
                break
            else:
                print("ingrese una opcion valida")
        except:
            print("ERROR")
    while True:
        try:
            pu=int(input("ingrese la cantidad de puertas: "))
            if pu>=2:
                listapuertas.append(pu)
                break
            else:
                print("ingrese una opcion valida")
        except:
            print("error")
    while True:
        try:
            trm=input("ingrese el tipo de transmision M o A: ")
            
            if trm=="M" or trm=="A":
                listatrm.append(trm)
                break
            else:
                print("INGRESE UNA OPCION VALIDA")
        except:
            print('ERROR')
    while True:
        try:
            color=input("ingrese el color: ")
            listacolor.append(color)
            print(f"{color}")
            break
            
        except:
            print("ERROR")
    while True:
        try:
            kil=int(input("ingrese el kilometraje: "))
            if kil>=0:
                listakm.append(kil)
                break
            else:
                print("error")
        except:
            print("Error")
    while True:
        try:
            precio=int(input("ingrese el precio de venta: "))
            if precio>0:
                listaprecio.append(precio)
                break
            else:
                print("error")
        except:
            print("error")
#validaciones            
def validarletras(nombre):
    letra=False
    numeros=["1","2","3","4","5","6","7","8","9","0"]
    for x in nombre:
        for y in numeros:
            if x==y:
                letra=True
    if letra==True:
        return False
    else:
        return True

def validarcorreo(mail):
    signoarroba=False
    signopunto=False
    largo=False
    for x in mail:
        if x=="@":
            signoarroba=True
        if x==".":
            signopunto=True
        if len(mail)>6:
            largo=True
    if signoarroba==True and signopunto==True and largo==True:
        return True
    else:
        return False
    
def validarpatente(patente,listapatente):
    repite=False
    for x in listapatente:
        if x==patente:
            repite=True
    if repite==True:
        return True
    else:
        return False
#almacenar todos los datos en 1 lista
def mostrarauto(listapatente,listaprop,listaruts,listatelefono,listacorreo,listayir,listacarga,listapuertas,listatrm,listacolor,listakm,listaprecio,listamarca,listamodelo):
    ip=0
    while ip!=4:
        menu2()
        try:
            ip=int(input("seleccione una opcion: "))
            if ip>0 and ip<5:
                if ip==1:
                    while True:
                        try:
                            my=int(input("ingrese el año que desea filtrar: "))
                            if my>0:
                                for x in range(len(listayir)):
                                    if listayir[x]==my:
                                        pos=x
                                        print(listapatente[pos],listaprop[pos],listaruts[pos],listatelefono[pos],listacorreo[pos],listayir[pos],listacarga[pos],listapuertas[pos],listatrm[pos],listacolor[pos],listakm[pos],listaprecio[pos],listamarca[pos],listamodelo[pos])
                                        
                                        
                                        
                                        
                                break
                            else:
                                print("ingrese un año valido")
                        except:
                            print("ingrese un valor numerico")
                        
                    
                if ip==2:
                    while True:
                        try:
                            kl=int(input("ingrese el kilometraje que desea filtrar: "))
                            if kl>0:
                                for x in range(len(listakm)):
                                    if listakm[x]==kl:
                                        pos=x
                                        print(listapatente[pos],listaprop[pos],listaruts[pos],listatelefono[pos],listacorreo[pos],listayir[pos],listacarga[pos],listapuertas[pos],listatrm[pos],listacolor[pos],listakm[pos],listaprecio[pos],listamarca[pos],listamodelo[pos])
                                        
                                        
                                        
                                        
                                break
                            else:
                                print("ingrese un año valido")
                        except:
                            print("ingrese un valor numerico")                    
                                             
                if ip==3:
                    while True:
                        try:
                            pr=int(input("ingrese el año que desea filtrar: "))
                            if pr>0:
                                for x in range(len(listaprecio)):
                                    if listaprecio[x]==pr:
                                        pos=x
                                        print(listapatente[pos],listaprop[pos],listaruts[pos],listatelefono[pos],listacorreo[pos],listayir[pos],listacarga[pos],listapuertas[pos],listatrm[pos],listacolor[pos],listakm[pos],listaprecio[pos],listamarca[pos],listamodelo[pos])
                                        
                                        
                                        
                                        
                                break
                            else:
                                print("ingrese un año valido")
                                print((listapatente,listaprop,listaruts,listatelefono,listacorreo,listayir,listacarga,listapuertas,listatrm,listacolor,listakm,listaprecio))
                        except:
                            print("ingrese un valor numerico")
                else:
                    print("saliste del menu 2")
                    
            else:
                print("error ingrese una opcion dentro del rango")   
        except:
            print("ingrese un numero")
def menu2():
    listamenu2=["mostrar por año","mostrar por kilometraje","mostrar por precio","salir"]
    for x in range(len(listamenu2)):
        print(f"{x+1}){listamenu2[x]}")
    
    