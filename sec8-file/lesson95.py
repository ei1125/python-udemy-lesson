# 書き込み読み込みモード

s = """\
AAA
BBB
CCC
DDD
"""
# w+で書き込みプラス読み込み
# with open('test.txt', 'w+') as f:
    # f.write(s)
    # f.seek(0)
    # print(f.read())

# 読み込んでさらに書き込みおk
with open('test.txt', 'r+') as f:
    print(f.read())
    f.seek(0)
    f.write(s)
