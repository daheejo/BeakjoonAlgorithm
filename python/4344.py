t=int(input())

for i in range(t):
    mlist=list(map(int, input().split()))
    mean=sum(mlist[1:])/mlist[0]
    cnt=0
    for x in mlist[1:]:
        if x > mean:
            cnt+=1
    result=cnt/mlist[0]*100
    print(f'{result:.3f}%') #f-string 표기; 소수점 셋째짜리까지 표현


