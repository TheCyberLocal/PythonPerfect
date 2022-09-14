from cProfile import run


def func_1():
    print('started func_1')
    print('calling subFunc_1')
    subFunc_1()
    print('program has finished')


def subFunc_1():
    print('compiling numbers')
    temp_str = ''
    for i in range(10000):
        print(i, end=' ')
        temp_str += str(i)
    print()
    print('calling subFunc_2')
    subFunc_2(temp_str)


def subFunc_2(txt):
    print(txt)


run("func_1()")
