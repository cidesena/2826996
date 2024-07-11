h=int(input('Ingrese hora'))
m=int(input('Ingrese minutos'))
s=int(input('Ingrese segundos'))
s+=1
if s>59:
   s=0
   m+=1
if m>59:
   m=0
   h+=1
if h>23:
   h=0
print('son las ',h,':',m,':',s)
print(f'son las {h}:{m}:{s}')

