import sys

num = int(sys.stdin.readline())
testlist=list(map(int,sys.stdin.readline().split()))
maxi=max(testlist)

newlist=[]
for i in testlist:
    newlist.append(i/maxi*100)
print(sum(newlist)/num)