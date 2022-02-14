arr = [3,4.1,6,4,8]

def selection(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if array[j]<array[min_index]:
                min_index = j
        array[i],array[min_index] = array[min_index], array[i]
        print(array[:i+1])

print('before: ', arr)
selection(arr)
print('after: ', arr)

#가장 작은 값을 찾아 맨 앞과 교환
#앞에서부터 정렬