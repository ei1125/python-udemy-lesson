# 関数の引数と返り値の宣言

# num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b

# r = add_num(10, 20)
r = add_num('a', 'b')
# エラーとして返してくれない
print(r)
