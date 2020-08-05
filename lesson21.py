# タプル型
# 代入できない
# 読み込み専用

t = (1, 2, 3, 4, 1, 2)
print(t)
print(type(t))

try:
 t[0] = 100
except:
  print('error')

print(t[0])
print(t[-1])

t = ([1,2,3],[4,5,6])
print(t)
t[0][0] = 100
print(t)

t = 1, 2, 3
print(type(t))
print(t)
t = 1,
print(type(t))
print(t)

new_tuple = (1, 2, 3) + (4, 5, 6)
print(new_tuple)

try:
  new_tuple = (1) + (4, 5, 6)
except:
  print('error')
# カンマをつければ足せる
new_tuple = (1,) + (4, 5, 6)
print(new_tuple)