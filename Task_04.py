# Деление шоколадки

# Определите, можно ли от шоколадки размером a × b долек отломить c долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Выведите yes или no соответственно.

# Пример:
# a, b, c = 3, 2, 4 -> yes
# a, b, c = 3, 2, 1 -> no

length = int(input('Введите длину шоколадки: '))
width = int(input('Введите ширину шоколадки: '))
pieces = int(input('Введите количество долек шоколадки, которые необходимо отломить: '))

if pieces < length * width and ((pieces % length == 0) or (pieces % width == 0)):
    print('YES')
else:
    print('NO')
