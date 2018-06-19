def logPrefix_1(str1):
    def decorator_1(f):
        return f

    return decorator_1


def logPrefix_2(str1, str2):
    print("consume 1st arg")

    def consume(str2):
        print("consume 2nd arg")

        def decorator_1(f):
            return f

        return decorator_1

    print("call inner method to consume 2nd arg")
    return consume(str2)


def logPrefix_3(str1, str2):
    print("consume all args")

    def decorator_1(f):
        return f

    return decorator_1


@logPrefix_3("@@@", "###")
def sum(a, b):
    return a + b


print(":::start:::")
print(sum(5, 8))
