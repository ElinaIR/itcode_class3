def Fibonacci(n):
    if n in [1, 2]:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)


n = int(input('Enter n\n'))
while n < 1:
    n = int(input('n must be > 0'))

print(Fibonacci(n))

