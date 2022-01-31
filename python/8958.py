import sys

t=int(sys.stdin.readline())

for i in range(t):
    oxlist=list(sys.stdin.readline())
    score=0
    sum_score=0 #점수와 점수의 합을 선언하고 0으로 세팅
    for ox in oxlist:
        if ox == 'O':
            score+=1
            sum_score+=score
        else:
            score=0
    print(sum_score)