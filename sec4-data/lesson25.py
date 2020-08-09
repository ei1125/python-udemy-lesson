# 辞書型のメソッド

d = {'x': 10, 'y': 20}
print(d)

# help(d)
# ヘルプを表示

print(d.keys())

print(d.values())

d2 = {'x': 1000, 'j': 500}
print(d2)

d.update(d2)
print(d)

print( "d.get('x')", d.get('x'))

print(d.get('z'))

print(d.pop('x'))
print(d)

del d['y']
print(d)

d = {'a': 100, 'b': 200}
d.clear()
print(d)
d = {'a': 100, 'b': 200}
print('a' in d)
# True
print('j' in d)
# False
