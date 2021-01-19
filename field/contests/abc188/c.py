提出 #19520095

ソースコード 

Copy
Copy
n=int(input())
a=list(int(x) for x in input().split())
m=0
s=1
for i in range(2**n-1):
        if a[m]>a[m+1]:
            a.append(a[m])
        if a[m]<a[m+1]:
            a.append(a[m+1])
        m+=2
if a[2**(n+1)-2]==a[2**(n+1)-3]:
    x=a[2**(n+1)-4]
    for i in a:
        if x==i:
            print(s)
            break
        else:
            s+=1
else:
    x=a[2**(n+1)-3]
    for i in a:
        if x==i:
            print(s)
            break
        else:
            s+=1
