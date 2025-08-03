test_arr1 = [-3, -2, 4] # true
test_arr2 = [-3, -4, -1] # false
test_arr3 = [14, 13, 2] # true
test_arr4 = [1, 4, 8] # true
test_arr5 = [1,2,3,5,2,10] # false


def is_monotonic_alt(arr):
    if len(arr) <=1:
        return True
    
    dir = 0
    for i in range(len(arr)):
        if i==0:
            continue
        if arr[i] > arr[i-1]:
            new_dir = 1
        elif arr[i] < arr[i-1]:
            new_dir = -1
        if (dir == 1 and new_dir == -1) or (dir == -1 and new_dir == 1):
            return False
        dir=new_dir
    return True


def is_monotonic(arr):
    left = arr[0]
    right = arr[len(arr)-1]

    if left < right:
        for i in range(len(arr)-1):
            if arr[i+1] < arr[i]:
                return False

    if left == right:
        for i in range(len(arr)-1):
            if arr[i+1] != arr[i]:
                return False

    if left > right:
        for i in range(len(arr)-1):
            if arr[i+1] > arr[i]:
                return False        

    return True


print(is_monotonic(test_arr1))
print(is_monotonic(test_arr2))
print(is_monotonic(test_arr3))
print(is_monotonic(test_arr4))
print(is_monotonic(test_arr5))
