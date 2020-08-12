# スタイルルール

# ダメな例
long_word = ""
for word in ['fdadf', ';skdga', 'gadfga']:
    long_word += "{}fdadfa".format(word)

# 良い例
long_word = ""
for word in ['fdadf', ';skdga', 'gadfga']:
    long_word.append("{}fasdag.format(word")
new_long_word = ''.join(long_word)

# 何もないときシングル
print('barbaanef')
# 何かあるときダブル
print("varnb'arvd")
"fdavadf {} fadvafa".format('test')

if x:
    print('exit')
else:
    print('else')

if x: print('exit')
else: print('else')

# クラスのときキャメルケース
# class RestaurantRobot(object):

# グローバル変数
# DEFAULT_ROBOT_NAME
