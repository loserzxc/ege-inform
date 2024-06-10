a=[int(x) for x in open('17_1970.txt')]
ans=[]
k=0
for i in range(len(a)-1):
    if (a[i]%3==0 or a[i+1]%3==0)>=1:
        ans.append(a[i]+a[i+1])
        k+=1
print(k,max(ans))
# 2802 1990
