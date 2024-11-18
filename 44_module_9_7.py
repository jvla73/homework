def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        is_prime = True
        for i in range(2, result):
            if result % i == 0:
                is_prime = False
        if is_prime:
            return (f'Простое\n{result}')
        else:
            return (f'Составное\n{result}')
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)