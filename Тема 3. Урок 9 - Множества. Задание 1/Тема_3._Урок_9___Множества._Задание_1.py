u=[]
s=input()
s=input()
for a in s.split():
    p=0
    for i in u:
        if i==a:
            p=1
            break
    if p==0:
        u+=[a]
print(len(u))