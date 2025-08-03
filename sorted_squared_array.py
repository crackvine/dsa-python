
test_arr1 = [0,1,3,5]
test_arr2 = [-6,-1,0,5,10]
test_arr3 = []

def sorted_squared_brute(arr):
    res = []
    for elem in arr:
        res.append(elem**2)
    res.sort()


def sorted_squared_alt(arr):
    res = [0] * len(arr)
    i = 0
    j = len(arr)-1
    k = len(arr)-1
    while i<=j:
        if arr[i]**2 < arr[j]**2:
            res[k] = arr[j]**2
            j=j-1
        else:
            res[k] = arr[i]**2
            i=i+1
        k=k-1
    print(res)


def sorted_squared(arr):
    res = [0] * len(arr)
    left = 0
    right = len(arr)-1
    for i in reversed(range(len(arr))):
        left_sq=arr[left]**2
        right_sq=arr[right]**2
        if left_sq<right_sq:
            res[i] = right_sq
            right-=1
        else:
            res[i] = left_sq
            left+=1
    print(res)


sorted_squared(test_arr1)
sorted_squared(test_arr2)
sorted_squared(test_arr3)
