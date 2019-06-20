class Fibonacci:
    def fib(num):
        f = 0
        s=1
        result=0
        for c in range(num):
            if c==1:
                print(c)    
            else:
                result = f + s
                f = s
                s = result
                print(result)

obj = Fibonacci
obj.fib(10)
