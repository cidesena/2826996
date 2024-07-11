min=1300000
#est=int(input('diga su estrato'))
est=input('diga su estrato')
match est:
    case '1':
        print('paga 0')    
    case '2':
        print(f'paga {min*0.10}')
    case '3':
        print(f'paga {min*0.20}')
    case '4':
        print(f'paga {min*0.30}')
    case '5':
        print(f'paga {min*0.40}')
    case '6':
        print(f'paga {min*0.50}')
    case _:
        print('La opción no existe')
    
# if est==1:
#     print(f'paga {0}')
# elif est==2:
#     print(f'paga {min*0.80}')
