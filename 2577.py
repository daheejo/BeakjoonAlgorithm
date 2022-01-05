import sys
a=int(sys.stdin.readline())
b=int(sys.stdin.readline())
c=int(sys.stdin.readline())
val=str(a*b*c)
print(val.count('0'),val.count('1'),val.count('2'),val.count('3'),
      val.count('4'),val.count('5'),val.count('6'),val.count('7'),
      val.count('8'),val.count('9'), sep="\n")  #.count() 메서드!