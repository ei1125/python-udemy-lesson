# 多重継承

class Person(object):
    def talk(self):
        print('talk')
    
    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

# class PersonCarRobot(Car, Person):
class PersonCarRobot(Person, Car):
    def fly(self):
        print('fly')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
# 左側の引数のクラスから先に実行される
person_car_robot.run()
person_car_robot.fly()