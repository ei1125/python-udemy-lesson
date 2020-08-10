# プロパティーを使った属性の設定

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        self.__enable_auto_run = enable_auto_run
        self.passwd = passwd
    # ある条件が合致したときだけ書き換える
    # 読み込みは出来るけど設定はできなくする（ゲッター）
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    # セッター
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__enable_auto_run)
        print('super fast')
    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('Model S', passwd='111')
# tesla_car.enable_auto_run = True
tesla_car.run()
# print(tesla_car.__enable_auto_run)

