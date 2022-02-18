arr = [4.7,9,21,0,8,6]

def merge(array):
    if len(array)<2:
        return array
    mid = len(array)//2
    lowArr= merge(array[:mid])
    highArr= merge(array[mid:])

    mergedArr=[]
    l = h = 0
    while l < len(lowArr) and h<len(highArr):
        if lowArr[l]<highArr[h]:
            mergedArr.append(lowArr[l])
            l +=1