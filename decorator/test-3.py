def logPrefix(str1):
    """带参数的装饰器函数。
    在函数前使用这个装饰器，会执行这个函数，返回并执行内部真正的装饰器。
    运行程序就可以发现在打印start前，logPrefix与real_decorator均被执行了。
    """
    print("do something in logPrefix")

    def real_decorator(f):
        print("do something in real_decorator")

        def new_F(*args, **kw):
            print(str1, " before user call function")
            result = f(*args, **kw)
            print(str1, " result of user function: ", result)
            print(str1, " after user call function")
            return result

        return new_F

    return real_decorator


@logPrefix("@@@")
def sum(a, b):
    return a + b


print(":::start:::")
print(sum(5, 8))
