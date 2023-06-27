import fun as fn
listapatente=[]
listaprop=[]
listaruts=[]
listatelefono=[]
listacorreo=[]
listayir=[]
listacarga=[]
listapuertas=[]
listatrm=[]
listacolor=[]
listakm=[]
listaprecio=[]
listamarca=[]
listamodelo=[]

op=0
while True:
    fn.menu()
    try:
        op=int(input("ingrese una opcion: "))
        if op>0 and op<6:
            if op==1:
                print("opcion 1")
                fn.op1(listapatente,listaprop,listaruts,listatelefono,listacorreo,listayir,listacarga,listapuertas,listatrm,listacolor,listakm,listaprecio,listamarca,listamodelo)
                
            elif op==2:
                print("opcion 2")
                fn.mostrarauto(listapatente,listaprop,listaruts,listatelefono,listacorreo,listayir,listacarga,listapuertas,listatrm,listacolor,listakm,listaprecio,listamarca,listamodelo)
            elif op==3:
                print("opcion 3")
            elif op==4:
                print("opcion 4")
            else:
                print("saliste del programa")
                break
        else:
            print("ingrese una opcion valida")   
    except:
        print("ingrese valor numerico")
        