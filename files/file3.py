# with open('files/prueba.txt','r')as f:
#     content=f.read()
#     print(type(content))
#     print(content)    

with open('files/prueba.txt','r',encoding='utf-8')as f:
    content=f.readline()
    print(type(content))
    print(content)

for linea in content:
    print(linea,'mide=',len(linea))
