import time
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
def fibonacci_caching(n, chache = None):
    if chache is None:
       chache = {}
    if n<=1:
        return n
    if n in chache:
        return chache[n]
    result = fibonacci_caching(n-1, chache)+ fibonacci_caching(n-2, chache)
    return result

def main():
    print("Programacion dinamica")

    start_time = time.time_ns()
    print(fibonacci(40))
    end_time =time.time_ns()
    print(f"time taken: {end_time - start_time} ns")

    start_time = time.time_ns()
    print(fibonacci_caching(40))
    end_time =time.time_ns()
    print(f"time taken: {end_time - start_time} ns")

if __name__=="__main__":
    main()