# pythonの書き方

# 良い例
d = {'key1': 'value1', 'key2': 'value2'}
if 'key1' in d:
    print('test')
# ダメな例
if 'key1' in d.keys():
    print('test')


# ジェネレーターで同じことできるならジェネレーターを使おう(
# 処理が早い)

def t():
    # num = []
    for i in range(10):
        yield i
    # return num

# for i in t():
#     print(i)

# if文の書き方バリエーション
y = None
x = 1 if y else 2
print(x)


# クロージャー
# グローバル変数を隠蔽できる

def base(x):
    def plus(y):
        return x + y
    return plus

plus = base(10)
print(plus(10))
print(plus(30))

i = 0
def add_num():
    def plus(y):
        return i + y
    return plus

i = 10
plus = add_num()
print(plus(10))
i = 100
print(plus(30))
