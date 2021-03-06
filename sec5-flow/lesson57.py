# デコレーター
# 関数を実行する前に処理を追加したい

def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result = func(*args, **kwargs)
        print('end')
        return result
    return wrapper

# 順序も大切
@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

# @print_info
# def sub_num(a, b):
#     return a - b

f = print_info(print_more(add_num))
r = f(10, 20)
print(r)

# f = print_info(add_num)
# r = f(10, 20)
# print(r)


# print('start')
# r = add_num(10, 20)
# print('end')

# print(r)
