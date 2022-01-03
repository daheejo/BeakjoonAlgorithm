import sys

N,X=map(int,sys.stdin.readline().split())
A=list(map(int, sys.stdin.readline().split()))
       
for i in range(N):
    if A[i]<X:
        print(A[i], end=" ")

        #end=" "를 잘 활용합시다!