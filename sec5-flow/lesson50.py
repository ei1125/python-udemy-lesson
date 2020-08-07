# 位置引数とキーワード引数とデフォルト引数

def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

# menu('beef', 'beer', 'ice')
# menu(entree='beef', dessert='ice', drink='beer')
menu('beef', dessert='ice', drink='beer')

# デフォルト引数
def menu2(entree='beef', drink='wine', dessert='ice'):
    print('entree =', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu2()
# 上書き可能
menu2(entree='chicken', drink='beer')
menu2('chicken', drink='beer')