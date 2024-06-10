a=[int(x) for x in open('17_1995.txt')]
ans=[]
k=0
for i in range(len(a)-1):
    if (a[i]+a[i+1])%2==0 and abs(a[i]+a[i+1])%10!=6:
        ans.append((a[i]+a[i+1])//2)
        k+=1
print(k,max(ans))
#1971 9702      
                             
