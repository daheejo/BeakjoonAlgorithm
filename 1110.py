import sys

n=int(sys.stdin.readline())
num=n #새로운 변수 num을 이미 등장한 변수 n에 저장하기
cnt=0 #사이클 수를 초기 0으로 지정하고 시작
while True:
    a=num//10 #몫(10의 자리)
    b=num%10 #나머지(1의 자리)
    c=(a+b)%10 # 즉 일의 자리만 필요한 경우 10으로 나눈 나머지를 구한다!
    num=(b*10)+c

    cnt+=1
    if (num==n):
        break

print(cnt)