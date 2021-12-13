class Fibo():
    
    def func_fibo(n):
        a = b = 1
        result = []
        for i in range(n):
            result.append(a)
            a = b
            b = a + b
        return result

    def generator_fibo(n):
        a = b = 1
        for i in range(n):
            yield a
            a = b
            b = a + b
