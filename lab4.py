
import timeit
import matplotlib.pyplot as plt
import random

def fact_recursive(n: int) -> int:
    '''Рекурсивный факториал'''
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact_recursive(n-1)


def fact_iterative(n: int) -> int:
    '''Итерактивный факториал'''
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact



def benchmark(function, n, repeat=10):
    """Возвращает среднее время выполнения func(n)"""
    times = timeit.repeat(lambda: function(n), number=5, repeat=repeat)
    return min(times)



def main():
    # фиксированный набор данных
    random.seed(52)
    test_data = list(range(1, 101))

    res_recursive = []
    res_iterative = []

    for n in test_data:
        res_recursive.append(benchmark(fact_recursive, n))
        res_iterative.append(benchmark(fact_iterative, n))

    # График
    plt.plot(test_data, res_recursive, label="Рекурсивный")
    plt.plot(test_data, res_iterative, label="Итеративный")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()


print()
