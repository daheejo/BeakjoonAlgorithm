import sys

a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
d=int(sys.stdin.readline())
e=int(sys.stdin.readline())
f=int(sys.stdin.readline())
g=int(sys.stdin.readline())
h=int(sys.stdin.readline())
i=int(sys.stdin.readline())

# 입력이 많을 때 코드 간결히 정리!!
#num_list = []
#for i in range(9):
    #num_list.append(int(input()))
    
li=[a, b, c, d, e, f, g, h, i]
ma=max(li)
print(ma, li.index(ma), sep="\n")  #인덱스 메서드!!