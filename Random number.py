import random
n1=int(input('随机数个数='))
n2=int(input('随机数长度='))
l=[]
s='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
while True:
    name=''
    for _ in range(n2):
        i=random.choice(s)
        name=name+i
    if name not in l:
        l.append(name)
        if len(l)==n1:
            for j in l:
                print(j)
            break
input('请按任意键继续. . .')