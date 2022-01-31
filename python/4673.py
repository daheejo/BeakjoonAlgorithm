def d(n):
    n = n + sum(map(int, str(n))) #str으로 정수 n을 한 글자씩 쪼개기
    return n

nonSelfNum = set() #중복 방지

for i in range(1,10001):
    nonSelfNum.add(d(i)) #set에 추가할 때는 add

for x in range(1,10001):
    if x not in nonSelfNum:
        print(x)
