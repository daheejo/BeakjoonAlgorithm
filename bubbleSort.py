arr = [9,8,7,6,5,4,3,2,1]

def bubble(array):
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1] = array[j+1],array[j]
        print(array)

print(arr)
bubble(arr)
print('after: ', arr)   

#인접한 두 수 비교