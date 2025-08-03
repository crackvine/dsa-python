test_arr1 = [2,7]
target1 = 9 #[0,1]

test_arr2 = [2,7,3,-1,4]
target2 = 2 # [2,3]

test_arr3 = [2,7,3,-1,4]
target3 = 100 # []

test_arr4 = [2,7,3,-1,4]
target4 = 25 # []

test_arr5 = []
target5 = 25 # []


def two_sum_brute(arr, k):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] + arr[j] == k:
                return [i,j]
    return []

def two_sum(arr, k):
    seen = {}
    for i in range(len(arr)):
        need = k - arr[i]
        if need in seen:
            return [seen[need], i]
        seen[arr[i]] = i
    return []



print(two_sum(test_arr1,target1))
print(two_sum(test_arr2,target2))
print(two_sum(test_arr3,target3))
print(two_sum(test_arr4,target4))
print(two_sum(test_arr5,target5))
