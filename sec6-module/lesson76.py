# importする際の記述の仕方
# １行ずつ書く、アルファベット順
# サードパーティーのには１行あける
# 標準、サード、セルフ、ローカル


import collections
import os
import sys

import termcolor

import lesson68_package

# import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson68_package.__file__)
# print(config.__file__)

print(sys.path)