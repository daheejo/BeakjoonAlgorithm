import sys #모듈 임포트

x=int(sys.stdin.readline()) #input()대신 시간 효율화

for i in range(x):
    a,b=map(int,sys.stdin.readline().split())
    print(a+b)