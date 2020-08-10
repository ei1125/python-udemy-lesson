# クラスメソッドとスタティックメソッド

def about(year):
    print('about human {}'.format(year))

class Person(object):

    kind = 'human'

    def __init__(self):
        self.x = 100
    
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

a = Person()
print(a.what_is_your_kind())
# オブジェクトを作らなくても呼び出せる
b = Person
print(b.kind)
print(b.what_is_your_kind())

Person.about(1999)
about(1999)