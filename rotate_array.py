test_arr1 = [1,2]
k1 = 1 # [2,1]

test_arr2 = []
k2 = 1 # []

test_arr3 = [1,3,5,6]
k3 = 2 # [5,6,1,3]

test_arr4 = [1,3,5,6]
k4 = 0 # [1,3,5,6]

def rotate_array(arr, k):
    length = len(arr)
    new = [0]*length
    for i in range(length):
        j = (i+k)%length
        new[j] = arr[i]
    return new


print(rotate_array(test_arr1, k1))
print(rotate_array(test_arr2, k2))
print(rotate_array(test_arr3, k3))
print(rotate_array(test_arr4, k4))
