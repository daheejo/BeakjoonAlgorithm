import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
val=str(a*b*c)
print(val.count('0'),val.count('1'),val.count('2'),val.count('3'),
      val.count('4'),val.count('5'),val.count('6'),val.count('7'),
      val.count('8'),val.count('9'), sep="\n")  #.count() 메서드!
#WEAKNESS#
#: print문에 val.count()의 반복.. this is NOT GOOD

## another solution ----------------------------------------------------
#val을 iterable한 객체로(여기선 list) 만들고 반복문 이용
# val=list(str(a*b*c)
# for i in range(10)  # 0-9
#     print(val.count(str(i)))
