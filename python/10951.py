import sys

#처음 썼던 오답
# a,b=map(int,sys.stdin.readline().split())
# while 0<a<10 and 0<b<10:
#     print(a+b) 

while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break

    #test case의 개수가 정해지지 않았으므로 try와 except 구문 활용!