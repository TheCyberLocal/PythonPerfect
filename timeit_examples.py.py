from timeit import timeit


def func_1():
    counter = 0
    for i in range(100):
        counter += 1


def func_2():
    counter = 0
    while counter < 100:
        counter += 1


print(timeit(func_1, number=10000))
print(timeit(func_2, number=10000))
