# 集合の使い所

my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

f = ['apple', 'banana', 'apple', 'banana']
# 型変換で重複削除
kind = set(f)
print(kind)
