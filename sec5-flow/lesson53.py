# キーワード引数の辞書化

def menu(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}

menu(**d)

def menu(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu('banana', 'apple', 'orange', entree='beef', drink='coffee')