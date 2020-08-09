# 組み込み関数

import builtins

builtins.print()

ranking = {
    'A' : 100,
    'B' : 85,
    'C' : 95
}

# for key in ranking:
#     print(key)

print(ranking.get('A'))

print(sorted(ranking, key=ranking.get, reverse=True))