test_arr1 = [1,5,6,3,4] #12
test_arr2 = [1,1,1] #1
test_arr3 = [10,6,5,6,5,7] #35
test_arr4 = [0] #0
test_arr5 = [100] #0
test_arr6 = [3,7,5,6,8,4] #21


def max_water_brute(arr):
    max = 0
    for x in range(len(arr)-1):
        for y in range(x, len(arr)):
            area = (min(arr[y],arr[x])) * (y-x)
            if area > max:
                max = area
    return max


def max_water(arr):
    max_area = 0
    left = 0
    right = len(arr)-1
    while left<right:
        h = min(arr[left], arr[right])
        w = right-left

        max_area = max(w*h, max_area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -=1
    return max_area


print(max_water(test_arr1))
print(max_water(test_arr2))
print(max_water(test_arr3))
print(max_water(test_arr4))
print(max_water(test_arr5))
print(max_water(test_arr6))

