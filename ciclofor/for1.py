num=int(input('ingrese numero'))
for i in range(1, num+1):
    if num%i==0:
        print(f'{i} es divisor')

num=1
sum=0
while num>0:
    num=int(input('ingrese numero'))
    sum+=num

print(f'la suma es {sum}')