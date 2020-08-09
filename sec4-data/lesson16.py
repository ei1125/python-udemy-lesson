l = [1, 20, 4, 50, 2, 1, 2]
print(l)
print(l[0])
print(l[1])
print(l[-1])
print(l[-2])
print(l[0:2])
print(l[:2])
print(l[2:5])
print(l[2:])
print(l[:])
print(len(l))
print(type(l))

print(list('abcdefg'))
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(n[::2])
# [1, 3, 5, 7, 9]
print(n[::-1])
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# ネスト
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[1])
print(x[0][2])