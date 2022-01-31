import sys

t=int(sys.stdin.readline())

for i in range(t):
    a,b=map(int,sys.stdin.readline().split())
    c=a+b
    print("Case #%s: %s + %s = %s"%(i+1, a, b, c ))

#출력 시 포맷팅 방식 잘 활용하기!