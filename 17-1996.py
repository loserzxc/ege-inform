a=[int(x) for x in open('17_1996.txt')]
ans=[]
k=0
for i in range(len(a)-1):
    if  abs(a[i]*a[i+1])%2!=0 and (abs(a[i]+a[i+1])//2)%7==0:
        ans.append((a[i]+a[i+1])//2)
        k+=1
print(k,min(ans))
# 179 -9107

