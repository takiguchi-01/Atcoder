N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0
 
for i in range(N):
  count += A[i] * B[i]
 
if count == 0:
  print ("Yes")
else:
  print ("No")
