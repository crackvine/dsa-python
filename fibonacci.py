n1 = 0 # 0
n2 = 1 # 1
n3 = 8 # 21
n4 = 12 # 


def fibonacci_simple(n, seen={}):
    if n<=1:
        return n
    return fibonacci_simple(n-1) + fibonacci_simple(n-2)



def fibonacci(n, seen={}):
    if n<=1:
        return n
    if n in seen:
        return seen[n]
    res = fibonacci(n-1, seen) + fibonacci(n-2, seen)
    seen[n] = res
    return res



print(fibonacci(n1))
print(fibonacci(n2))
print(fibonacci(n3))
print(fibonacci(n4))
