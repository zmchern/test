def fib(n):
    a,b =0,1
    print(a)
    while b<n:
        print(b,end="")
        a,b=b,a+b
        print("")
    print()

fib(1000)