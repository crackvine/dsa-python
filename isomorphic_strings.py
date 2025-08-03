test1_a = "ababa"
test1_b = "eoeoo" # false

test2_a = "cdc"
test2_b = "ede" # true

test3_a = "ghiiik"
test3_b = "efdedh" # false

test4_a = "h"
test4_b = "i" # true

test5_a = "ere"
test5_b = "a" # false

test6_a = "ab"
test6_b = "cc" # false

def isomorphic_strings(str1, str2):
    if len(str1) != len(str2):
        return False
    seen1 = {}
    seen2 = {}
    for i in range(len(str1)):
        if str1[i] in seen1 and str2[i] != seen1[str1[i]]:
            return False
        if str2[i] in seen2 and str1[i] != seen2[str2[i]]:
            return False
        seen1[str1[i]] = str2[i]
        seen2[str2[i]] = str1[i]

    return True

    
print(isomorphic_strings(test1_a, test1_b))
print(isomorphic_strings(test2_a, test2_b))
print(isomorphic_strings(test3_a, test3_b))
print(isomorphic_strings(test4_a, test4_b))
print(isomorphic_strings(test5_a, test5_b))
print(isomorphic_strings(test6_a, test6_b))
