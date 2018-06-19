def log(f):
    """一个装饰器函数。
    在函数前使用这个装饰器，会立即执行。
    因此在调用sum前打印语句就会执行。
    """
    print("do something in decorator")
    return f


@log
def sum(a, b):
    return a + b


print(":::start:::")
print(sum(5, 8))
