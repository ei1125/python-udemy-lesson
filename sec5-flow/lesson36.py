y = [1, 2, 3]
x = 1

if x in y:
  print('in')

if 100 not in y:
  print('not in')

# a = 1
# b = 2

# if not a == b:
#   print('Not equal')

# if a != b:
#   print('Not equal')

is_ok = True

if not is_ok:
  print('hello')

# 空かどうかも判定できる
is_ok = []
# False, 0, 0.0, '', [], (), {}, set()
if is_ok:
  print('OK!')
else:
  print('No!')