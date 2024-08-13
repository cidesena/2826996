from usuario import *
#nombre, regional, doc, telefono, mail
sel=0

while sel!=4:  
    print('1-Guardar datos de usuario')
    print('2-Ver usuarios')
    print('3-Instanciar usuario')
    print('4-salir')      
    sel=int(input('seleccione opcion'))
     
    match sel:
        case 1:
            print('Solicitar datos de usuario')
            n=input('ingrese nombre')
            r=input('ingrese regional')
            d=input('ingrese documento')
            t=input('ingrese telefono')
            m=input('ingrese mail')
#ob=Usuario(n,r,d,t,m)
            cad=f'{n} {r} {d} {t} {m}\n'
            with open('classes/usuario.txt','a') as f:
                f.write(cad)
        case 2:
            with open('classes/usuario.txt','r') as f:
                data=f.readlines()
                print(data)
        case 3:
             objetos=[]
             with open('classes/usuario.txt','r') as f:
                data=f.readlines()
                print(data)
                            
             for linea in data:
                apr=linea.split()
                n=apr[0]
                r=apr[1]
                d=apr[2]
                t=apr[3]
                m=apr[4]
                ob=Usuario(n,r,d,t,m)
                objetos.append(ob)
             print(objetos)
                 


