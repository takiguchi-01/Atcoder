N = int(input())
list_x = []
list_y = []

d = 0

for i in range(N):
    x, y = map(int, input().split())
    list_x.append(x)
    list_y.append(y)

for i in range(N):
    a=list_x[i]
    b=list_y[i]
    for j in range(N):
        if j==i:
            break
        c=(b-list_y[j])/(a-list_x[j])
        if -1<=c:
            if 1>=c:
                d+=1
print(d)
