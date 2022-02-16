arr=[1,4,6,5,8,2]

def insertion(array):
    n = len(array)
    for i in range(1,n):
        for j in range(1,0,-1):
            if array [j-1]>array[j]:
                array[j-1],array[j]=array[j],array[j-1]
        print(array[:i+1])

print("before: ", arr)
insertion(arr)
print("after: ",arr)