X,Y = map(int, input().split())
if X > Y:
  Y += 3
  if Y > X:
    print ('Yes')
  else:
    print ('No')
else:
  X += 3
  if X > Y:
    print ('Yes')
  else:
    print ('No')
