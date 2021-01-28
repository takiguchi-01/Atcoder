N,A,B = map(int, input().split())
 
C = A + B
R = N // C #ブロックの数(A+B)
amari = N % C #NをCで割った時のあまりの数
B_count = (min(A, amari)) #あまりの数がAより少なければ、amariを代入。それ以上だと赤ボールも含まれる為A(青ボール最大値)を代入
 
print(A*R+B_count)
