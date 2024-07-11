def num_perfectos(numerito):
    
    
    suma=0
    
    for i in range(1,numerito):
        
        if numerito % i == 0:
            
                    suma+=i
    
    if numerito== suma: 
    
        return 'Perfecto'
    
    else: 
    
        return "no es perfecto"
         

numerito= int (input("oiga señor digite un numero:"))
print(num_perfectos(numerito))

# if num_perfectos(numerito):
#       print('perfecto')
# else:
#       print('no perfecto')


    
    
    
    
    
