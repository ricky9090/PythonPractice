def log(f):
    """装饰器函数。
    在函数前使用这个装饰器，会立即执行打印do something。
    然后返回一个包含原函数的新函数new_F。
    通过原函数名调用时，实际执行的是新函数new_F，
    因此可以看到添加的打印before,after
    """
    print("do something in decorator")

    def new_F(*args, **kw):
        print("    before user call function")
        result = f(*args, **kw)
        print("    result of user function: ", result)
        print("    after user call function")
        return result

    return new_F


@log
def sum(a, b):
    return a + b


print(":::start:::")
print(sum(5, 8))
