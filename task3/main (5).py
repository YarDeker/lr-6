
def fibonacci_up_to_n(n):
    fib_nums = set()
    a, b = 0, 1
    while a <= n:
        fib_nums.add(a)
        a, b = b, a + b
    return fib_nums


def check_fibonacci_in_set():
    number_set = set(range(1, 51))
    
    fib_numbers = fibonacci_up_to_n(50)
    
    fib_in_set = number_set.intersection(fib_numbers)
    
    if not isinstance(number_set, set):
        number_set = set(list(number_set))
    
    print("Числа Фібоначчі, що знаходяться в діапазоні від 1 до 50:")
    print(fib_in_set)
    print(f"Кількість таких чисел: {len(fib_in_set)}")

check_fibonacci_in_set()
