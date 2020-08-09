# 名前空間とスコープ

"""
Test Test #######################
"""
animal = 'cat'

def f():
    """Text func doc"""
    # print(animal)
    # global animal
    # animal = 'dog'
    # print('after:', animal)
    # print('local:', locals())
    print(f.__name__)
    print(f.__doc__)

f()
print('global:', animal)
# print('global:', globals())
print(__name__)

