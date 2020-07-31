print('a is {}'.format('a'))
print('a is {}'.format('test'))
print('a is {} {} {}'.format(1, 2, 3))
print('a is {0} {1} {2}'.format(1, 2, 3))
print('a is {2} {1} {0}'.format(1, 2, 3))

print('My name is {0} {1}'.format('Ei', 'Morishita'))

print('My name is {name} {family}'.format(name='Ei', family='Morishita'))

print("#######################")
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Ei'
family = 'Morishita'
print(f'My name is {name} {family}. Watashi ha {family} {name}')
