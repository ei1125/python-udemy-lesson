# 関数定義

# def say_something():
#     print('hi')

# say_something()

# print(type(say_something))

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('green')
print(result)
result = what_is_this('red')
print(result)
result = what_is_this('blue')
print(result)