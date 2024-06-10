a=[int(x) for x in open('17_1998.txt')]
ans=[]
k=0
for i in range(len(a)-2):
    if abs(a[i]*a[i+1]*a[i+2])%7==0 and (a[i]+a[i+1]+a[i+2])%10==5:
        k+=1
        ans.append(a[i]+a[i+1]+a[i+2])
print(k,max(ans))

#153 19285
