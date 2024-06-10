a=[int(x) for x in open('17_1993.txt')]
ans=[]
k=0
for i in range(len(a)-1):
    if abs( (a[i]*a[i+1])>0)and (a[i]+a[i+1])%7==0:
        ans.append(a[i]*a[i+1])
        k+=1
print(k,min(ans))
# 359 115022
