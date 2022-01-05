numlist=[]
rest=[]
#-----------------------------------
for i in range(10):
    numlist.append((int(input())))
for x in numlist:
    rest.append(x%42)
#------------------------------------
#or
# for in range(10):
    #n=int(input())
    #numlist.append(n%42) for 문 2번 쓸 필요없이 그냥 한꺼번에
#print(lent(set(numlist)))
final=set(rest) #중복을 허용하지 않는 set!
print(len(final))