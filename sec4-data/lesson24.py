# 辞書型

d = {'x': 10, 'y': 20}
print(d)
print(d['x'])
print(d['y'])

d['x'] = 100
print(d)
d['x'] = 'xxx'
print(d)
d['z'] = 200
print(d)

d[1] = 10000
print(d)

d2 = dict(a=10, b=20)
print(d2)

d3 = dict([('a', 10), ('b', 20)])
print(d3)
