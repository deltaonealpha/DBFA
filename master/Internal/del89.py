fib = (lambda x:x if x<=1 else fib(x-1) + fib(x-2))

for i in range(11):
    print(fib(i))