print('hello')
print("hello")
print("I don't know")
# print('I don't know'')
# /opt/anaconda3/bin/python /Users/hitoshi/PycharmProjects/python_programming/lesson.py
#   File "/Users/hitoshi/PycharmProjects/python_programming/lesson.py", line 4
#     print('I don't know'')
#                  ^
# SyntaxError: invalid syntax
#
# Process finished with exit code 1
print('I don\'t know')
print("say \"I don't know\"")

print('hello. \nHow are you?')

print('C:\name\name')
# C:
# ame
# ame
print(r'C:\name\name')
# C:\name\name


print("""
line1
line2
line3
""")
#
# line1
# line2
# line3
#

print("""######""")
print("""
line1
line2
line3
""")
print("""##########""")
# ######
#
# line1
# line2
# line3
#
# ##########

print("""######""")
print("""\
line1
line2
line3\
""")
print("""##########""")

# ######
# line1
# line2
# line3
# ##########

print("Hi." * 3)
# Hi.Hi.Hi.

print('Hi.' * 3 + 'Mike.')
# Hi.Hi.Hi.Mike.

print('Py' + 'thon')
# Python

print('Py''thon')

print('Py''thon')
prefix = 'Py'
# print(prefix'thon')
# #     print(prefix'thon')
# #                 ^
# # SyntaxError: invalid syntax
print(prefix + 'thon')
# Python

s = ('aaaaaaaaaaaaaaaaPy'
     'bbbbbbbbbbbbbbbbbb')
print(s)
# aaaaaaaaaaaaaaaaPybbbbbbbbbbbbbbbbbb

s = 'aaaaaaaaaaaaaaaaPy' \
    'bbbbbbbbbbbbbbbbbb'
print(s)
# aaaaaaaaaaaaaaaaPybbbbbbbbbbbbbbbbbb


###

word = 'python'
print(word[0])
print(word[1])
print(word[-1])
print(word[0:2])
print(word[2:5])
print('########')
print(word[0:2])
print(word[:2])
print('########')
print(word[2:])
# print(word[100])
# #     print(word[100])
# # IndexError: string index out of range
print('########')
# word[0] = 'j'
# #     word[0] = 'j'
# # TypeError: 'str' object does not support item assignment

word = 'j' + word[1:]
print(word)
# jython
print(word[:])
# jython
n = len(word)
print(n)
# 6

###

s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
# True
is_start = s.startswith('X')
print(is_start)
# False
print("#######")

print(s.find('Mike'))
# 11 前から１１番目
print(s.rfind('Mike'))
# 20 前から２０番目　後ろから
print(s.count('Mike'))
# 2
print(s.capitalize())
# My name is mike. hi mike.
print(s.title())
# My Name Is Mike. Hi Mike.

print(s.upper())
# MY NAME IS MIKE. HI MIKE.
print(s.lower())
# my name is mike. hi mike.

print(s.replace('Mike', 'Nancy'))
###

# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 'a is {}'.format('a')
# 'a is a'
# >>> 'a is {}'.format('test')
# 'a is test'
# >>> 'a is {} {} {}'.format(1,2,3)
# 'a is 1 2 3'
# >>> 'a is {0} {1} {2}'.format(1,2,3)
# 'a is 1 2 3'
# >>> 'a is {2} {1} {0}'.format(1,2,3)
# 'a is 3 2 1'
# >>> 'My name is {0} {1}'.format('Jun', 'Sakai')
# 'My name is Jun Sakai'
# >>> 'My name is {0} {1}. Watashi ha {1} {0}'.format('Jun', 'Sakai')
# 'My name is Jun Sakai. Watashi ha Sakai Jun'
# >>> 'My name is {name} {family}. Watashi ha {family} {name}'.format(name='Jun', family='Sakai')
# 'My name is Jun Sakai. Watashi ha Sakai Jun'
# >>> 1
# 1
# >>> '1'
# '1'
# >>> str(1)
# '1'
# >>> x = str(1)
# >>> type(x)
# <class 'str'>
# >>> str(3.14)
# '3.14'
# >>> str(True)
# 'True'
# >>> exit()
# (base)


###

# format -> f-strings
a = 'a'
print(f'a is {a}')
# a is a

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')
# a is 1, 2, 3
# a is 3, 2, 1

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. Watashi ha {family} {name}.')
# My name is Jun Sakai. Watashi ha Sakai Jun.

###

# print(2+2)

# import math
#
# result = math.sqrt(25)
# print(result)



###


# 15:00:02 hitoshi:~/PycharmProjects/python_programming (section_3_bssics_of_python)$
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 2+2
# 4
# >>> 5 - 2
# 3
# >>> 5*6
# 30
# >>> 50-5*6
# 20
# >>> (50-5)*6
# 270
# >>> 8/5
# 1.6
# >>> type(1)
# <class 'int'>
# >>> type(1.6)
# <class 'float'>
# >>> 0.6
# 0.6
# >>> .6
# 0.6
# >>> 17/3
# 5.666666666666667
# >>> 17//3
# 5
# >>> 17 % 3
# 2
# >>> 5 * 5
# 25
# >>> 5**2
# 25
# >>> 5*5*5*5*5
# 3125
# >>> 5**5
# 3125
# >>> x = 5
# >>> x
# 5
# >>> y = 10
# >>> x * y
# 50
# >>> a
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# >>> pie = 3.1415151515
# >>> pie
# 3.1415151515
# >>> round(pie,2)
# 3.14
# >>> exit()
# (base)




###

# print('Hi')
# print('Hi', 'Mike', sep=',')
#
# print('Hi', 'Mike', sep=',', end='\n')
# print('Hi', 'Mike', sep=',', end='\n')
#
# print('Hi', 'Mike', sep=',', end='')
# print('Hi', 'Mike', sep=',', end='')
#
# print('Hi', 'Mike', sep=',', end='.\n')
# print('Hi', 'Mike', sep=',', end='.\n')

###

# _num1 = 1
#
# # if = 'value'

# num = 1
# name = '1'
#
# new_num = int(name)
#
# print(new_num, type(new_num))



# num = 1
# name = 'Mike'
#
# num =name
#
# print(num,type(num))



# num = 1
# name = 'Mike'
# is_ok = True
#
# print(num, type(num))
# print(name, type(name))
# print(is_ok, type(is_ok))


# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> l = [1, 20, 4, 50, 2, 1, 2]
# >>> l
# [1, 20, 4, 50, 2, 1, 2]
# >>> l[0]
# 1
# >>> l[1]
# 20
# >>> l[-1]
# 2
# >>> l[-2]
# 1
# >>> l[0:2]
# [1, 20]
# >>> l[:2]
# [1, 20]
# >>> l[2:5]
# [4, 50, 2]
# >>> l[2:]
# [4, 50, 2, 1, 2]
# >>> l[:]
# [1, 20, 4, 50, 2, 1, 2]
# >>> len(l)
# 7
# >>> type(l)
# <class 'list'>
# >>> list('abcdefg')
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> l
# [1, 20, 4, 50, 2, 1, 2]
# >>> l[100]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range
# >>> n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> n
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> n[::2]
# [1, 3, 5, 7, 9]
# >>> n[::-1]
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# >>> a = ['a', 'b, 'c']
#   File "<stdin>", line 1
#     a = ['a', 'b, 'c']
#                    ^
# SyntaxError: invalid syntax
# >>> a = ['a', 'b', 'c']
# >>> n = [1, 2, 3]
# >>> x = [a, n]
# >>> x
# [['a', 'b', 'c'], [1, 2, 3]]
# >>> x[0]
# ['a', 'b', 'c']
# >>> x[1]
# [1, 2, 3]
# >>> x[0][1]
# 'b'
# >>> x[1][2]
# 3
# >>> exit()
# (base)

###

# $ python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> s
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> s[0]
# 'a'
# >>> s[0]='X'
# >>> s
# ['X', 'b', 'c', 'd', 'e', 'f', 'g']
# >>> s[2:5]
# ['c', 'd', 'e']
# >>> s[2:5]=['C', 'D', 'E']
# >>> s
# ['X', 'b', 'C', 'D', 'E', 'f', 'g']
# >>> s[2:5] = []
# >>> s
# ['X', 'b', 'f', 'g']
# >>> s[:]
# ['X', 'b', 'f', 'g']
# >>> s[:] = []
# >>> s
# []
# >>> n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> n
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> n.append(100)
# >>> n
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
# >>> n.insert(0, 200)
# >>> n
# [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100]
# >>> n.pop()
# 100
# >>> n
# [200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> n.pop(0)
# 200
# >>> n
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> del n[0]
# >>> n
# [2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> del n
# >>> n
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'n' is not defined
# >>> n = [1, 2, 2, 2, 3]
# >>> n.remove(2)
# >>> n
# [1, 2, 2, 3]
# >>> n
# [1, 2, 2, 3]
# >>> n.remove(2)
# >>> n.remove(2)
# >>> n
# [1, 3]
# >>> n.remove(2)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: list.remove(x): x not in list
# >>> a = [1, 2, 3, 4, 5]
# >>> b = [6, 7, 8, 9, 10]
# >>> a
# [1, 2, 3, 4, 5]
# >>> b
# [6, 7, 8, 9, 10]
# >>> x = a + b
# >>> x
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> a
# [1, 2, 3, 4, 5]
# >>> b
# [6, 7, 8, 9, 10]
# >>> a +=b
# >>> a
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> x = [1,2,3,4,5]
# >>> y=[6,7,8,9,10]
# >>> x.extend(y)
# >>> x
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> exit()
# (base)


###


r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3))
# 2
print(r.index(3, 3))
# 7
print(r.count(3))
# 2
if 5 in r:
    print('exist')
# exist
if 100 in r:
    print('exist')
#

r.sort()
print(r)
# [1, 1, 2, 2, 3, 3, 4, 5]

r.sort(reverse=True)
print(r)
# [5, 4, 3, 3, 2, 2, 1, 1]

r.reverse()
print(r)
# [1, 1, 2, 2, 3, 3, 4, 5]

s = 'My name is Mike.'
to_split = s.split(' ')
print(to_split)
# ['My', 'name', 'is', 'Mike.']

x = ' '.join(to_split)  # 空白文字を使ってリストを作って
print(x)
# My name is Mike.

print(help(list))





###


i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j=', j)
print('i=', i)
# j = [100, 2, 3, 4, 5]
# i = [100, 2, 3, 4, 5]

# 値渡しと参照渡し

x = [1, 2, 3, 4, 5]
y = x.copy() #  明示的にcopyを使ったほうが他の人からもわかりやすい
# y= x[:]
y[0] = 100
print('y=', y)
print('x =', x)
# y = [100, 2, 3, 4, 5]
# x = [1, 2, 3, 4, 5]

X = 20
Y = X
Y = 5
print(Y)
print(X)
# 5
# 20

X = 20
Y = X
Y = 5
print(id(Y))
print(id(X))
# 4455635424
# 4455635904


X = [ 'a', 'b']
Y = X
Y[0] = 'p'
print(id(Y))
print(id(X))
# 140404910750720
# 140404910750720
print(Y)
print(X)
# ['p', 'b']
# ['p', 'b']
# 両方書き換えられる



###


# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> seat = []
# >>> min = 0
# >>> max = 5
# >>> min <= len(seat) < max
# True
# >>> seat.append('p')
# >>> min <= len(seat) < max
# True
# >>> len(seat)
# 1
# >>> seat.append('p')
# >>> min <= len(seat) < max
# True
# >>> seat.append('p')
# >>> seat.append('p')
# >>> len(seat)
# 4
# >>> min <= len(seat) < max
# True
# >>> seat.append('p')
# >>> min <= len(seat) < max
# False
# >>> len(seat)
# 5
# >>> seat.pop(0)
# 'p'
# >>> min <= len(seat) < max
# True
# >>> exit()
# (base)


###

# tuple　はデータを変更できないようにしたいとき　
# 追加・変更　できない

# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> t = (1, 2, 3, 4, 1, 2)
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> t[0] = 100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> t[0]
# 1
# >>> t
# (1, 2, 3, 4, 1, 2)
# >>> t.index(1)
# 0
# >>> t.count(1)
# 2
# >>> t.help
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'tuple' object has no attribute 'help'
# >>> help(list)
#
# >>> help(tapple)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'tapple' is not defined
# >>> help(taple)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'taple' is not defined
# >>> help(tuple)
#
# >>> t = ([1,2,3], [4,5,6])
# >>> t
# ([1, 2, 3], [4, 5, 6])
# >>> t[0] = [1]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'tuple' object does not support item assignment
# >>> t[0][0]
# 1
# >>> t[0][0] = 100
# >>> t
# ([100, 2, 3], [4, 5, 6])
# >>> t = 1, 2, 3
# >>> type(t)
# <class 'tuple'>
# >>> t = 1,
# >>> t
# (1,)
# >>> type(t)
# <class 'tuple'>
# >>> t = 1
# >>> type(t)
# <class 'int'>
# >>> t=()
# >>> type(t)
# <class 'tuple'>
# >>> t = (1)
# >>> t
# 1
# >>> type(t)
# <class 'int'>
# >>> t = ('test')
# >>> type(t)
# <class 'str'>
# >>> t = ('test',)
# >>> t
# ('test',)
# >>> type(t)
# <class 'tuple'>
# >>>
# >>> t = 1,
# >>> t +100
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: can only concatenate tuple (not "int") to tuple
# >>> new_tupple = (1, 2, 3) + (4, 5, 6)
# >>> new_tupple
# (1, 2, 3, 4, 5, 6)
# >>>
# >>> new_tupple = (1) + (4, 5, 6)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'tuple'
# >>> new_tuple = (1,)+(4,5,6)
# >>> new_tuple
# (1, 4, 5, 6)
# >>> exit()
# (base)


####


num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = (10, 20)
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

a, b, c, d, e, f = "Mike", "1", "1", "1", "1", "1"
a = "Mike"
b = "1"
# あまり長めにするのは好まれない

i = 10
j = 20
tmp = i
i = j
j = tmp
print(i, j)

a = 100
b = 200
a, b = b, a
print(a, b)



###
# 質問をユーザーに投げかけて選択肢を３つ上げて２つ選択させるアプリ

chose_from_two = ('A', 'B', 'C')
# tupleではなく、配列を使ってしまうと間違えて操作してしまう可能性あり
# tuple にappendはできない
answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)


###

# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> d = {'x': 10, 'y': 20}
# >>> d
# {'x': 10, 'y': 20}
# >>> type(d)
# <class 'dict'>
# >>> d['x']
# 10
# >>> d['y']
# 20
# >>> d['x'] = 100
# >>> d
# {'x': 100, 'y': 20}
# >>> d['x'] = 'xxx'
# >>> d
# {'x': 'xxx', 'y': 20}
# >>> d['z'] = 200
# >>> d
# {'x': 'xxx', 'y': 20, 'z': 200}
# >>> d[1] = 10000
# >>> d
# {'x': 'xxx', 'y': 20, 'z': 200, 1: 10000}
# >>> dict(a=10,b=20)
# {'a': 10, 'b': 20}
# >>> dict([('1',10),('b', 20)])
# {'1': 10, 'b': 20}
# >>> exit()
# (base)


###

# $
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> d = ('x':10,'y':20)
#   File "<stdin>", line 1
#     d = ('x':10,'y':20)
#             ^
# SyntaxError: invalid syntax
# >>> d = ('x': 10, 'y': 20)
#   File "<stdin>", line 1
#     d = ('x': 10, 'y': 20)
#             ^
# SyntaxError: invalid syntax
# >>> d = ('x': 10, 'y': 20)
#   File "<stdin>", line 1
#     d = ('x': 10, 'y': 20)
#             ^
# SyntaxError: invalid syntax
# >>> d = {'x': 10, 'y': 20}
# >>> d
# {'x': 10, 'y': 20}
# >>> d.keys()
# dict_keys(['x', 'y'])
# >>> d.values()
# dict_values([10, 20])
# >>> d2 = {'x': 1000, 'j': 500}
# >>> d
# {'x': 10, 'y': 20}
# >>> d2
# {'x': 1000, 'j': 500}
# >>> d.update(d2)
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d['x']
# 1000
# >>> d.get('x')
# 1000
# >>> d['z']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'z'
# >>> r = d.get('x')
# >>> r
# 1000
# >>> r = d.get('z')
# >>> r
# >>> type(r)
# <class 'NoneType'>
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d.get('x')
# 1000
# >>> d
# {'x': 1000, 'y': 20, 'j': 500}
# >>> d.pop('x')
# 1000
# >>> d
# {'y': 20, 'j': 500}
# >>> del d['y']
# >>> d
# {'j': 500}
# >>> del d
# >>> d
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'd' is not defined
# >>> d = {'a': 100, 'b': 200}
# >>> d
# {'a': 100, 'b': 200}
# >>> d.clear()
# >>> d
# {}
# >>> d = {'a': 100, 'b': 200}
# >>> d
# {'a': 100, 'b': 200}
# >>> 'a' in d
# True
# >>> 'j' in d
# False
# >>> exit()
# (base)

x = {'a': 1}
y = x
y['a'] = 1000
print(x)
print(y)

x = {'a': 1}
y = x.copy()
y['a'] = 1000
print(x)
print(y)


####
# List よりも Hash テーブルのほうが早い
l = [
    ['apple', 100],
    ['banana', 100],
    ['orange', 100],
]
print(l[0][1])

fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}

print(fruits['apple'])


###

# $
#  clear
# (base)
# 13:15:54 hitoshi:~/PycharmProjects/python_programming (section_3_bssics_of_python *)$
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> a = {1, 2, 2, 3, 4, 4, 4, 5, 6}
# >>> a
# {1, 2, 3, 4, 5, 6}
# >>> type(a)
# <class 'set'>
# >>> b = {2,3,3,6,7}
# >>> b
# {2, 3, 6, 7}
# >>> a
# {1, 2, 3, 4, 5, 6}
# >>> a-b
# {1, 4, 5}
# >>> b-a
# {7}
# >>> a & b
# {2, 3, 6}
# >>> a + b
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'set' and 'set'
# >>> a | b
# {1, 2, 3, 4, 5, 6, 7}
# >>> a ^ b
# {1, 4, 5, 7}
# >>> exit()
# (base)



####

# $
#  clear
# (base)
# 13:20:27 hitoshi:~/PycharmProjects/python_programming (section_3_bssics_of_python)$
#  python
# Python 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] :: Anaconda, Inc. on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> s = {1,2,3,4,5}
# >>> s
# {1, 2, 3, 4, 5}
# >>> s[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable
# >>> s.add(6)
# >>> s
# {1, 2, 3, 4, 5, 6}
# >>> s.add(6)
# >>> s
# {1, 2, 3, 4, 5, 6}
# >>> s.remove(6)
# >>> s
# {1, 2, 3, 4, 5}
# >>> s.clear()
# >>> s
# set()
# >>> a = {}
# >>> type(a)
# <class 'dict'>
# >>> a
# {}
# >>> type(a)
# <class 'dict'>
# >>> help(set)
#
# >>> exit()
# (base)

###

my_friends = {'A', 'C', 'D'}
A_friends = {'B','D','E','F'}
print(my_friends & A_friends)
# Aさんと私の共通の友達

f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)


###

print('XXXXXX')
"""
test
test
test
test
"""
print('XXXXXX')

# Apple price
some_value = 100

###

s = 'aaaaaa' \
    + 'bbbbbbb'
print(s)
# 折返しは \ をつかう
x = 1 + 1 + 1 + 1 + 1 + 1 + 1 \
    + 1 + 1 + 1 + 1 + 1 + 1 + 1
print(x)
# 80文字　以上になる場合は次の行に行く
x = (1 + 1 + 1 + 1 + 1 + 1 + 1
     + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)

####


x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')



###

a = 1
b = 1

a == b
a != b
a < b
a > b
a <= b
a >= b
a > 0 and b > 0
a > 0 or b > 0



###

y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

# a = 1
# b = 2
#
# if not a == b:
#     print('Not equal')
#
# if a != b:
#     print('Not equal')

is_ok = True

if is_ok:
    print('hello')

if not is_ok:
    print('hello')


####

is_ok = True
if is_ok:
    print('OK')
#  OK

is_ok = 1
if is_ok:
    print('OK')
# OK

is_ok = 10020
if is_ok:
    print('OK!')
else:
    print('No!')
# OK!

is_ok = 0
if is_ok:
    print('OK!')
else:
    print('No!')
# No!

is_ok = ''
if is_ok:
    print('OK!')
else:
    print('No!')
# No!

is_ok = []
if is_ok:
    print('OK!')
else:
    print('No!')
# No!

is_ok = [1, 2, 3, 4]
if is_ok:
    print('OK!')
else:
    print('No!')
# OK!

# False, 0, 0, 0, '', [], {}, (), set()


###
is_empty = None
print(is_empty)
# print(help(is_empty))

if is_empty == None:
    print('None!!!')

if is_empty is None:
    print('None!!!')

if is_empty is not None:
    print('YES!!!')

print(1 == True)    # 真どうしか？
print(1 is True)    # オブジェクト同士　が　同じか？
print(True is True)

a = None
print(a is None)


###

# count = 0
#
# while count < 5:
#     print(count)
#     count += 1

# while True:
#     print('XXX')

# count = 0
# while True:
#     if count >= 5:
#         break
#
#     if count == 2:
#         count += 1
#         continue
#
#     print(count)
#     count += 1
# # 0
# # 1
# # 3
# # 4


# count = 0
#
# while count < 5:
#     if count == 1:
#         break
#     print(count)
#     count += 1
# else:
#     print('done')
#
#


# while True:
#     word = input('Enter')
#     if word == 'ok':
#         break
#     print('next')




# some_list = [1, 2, 3, 4, 5]
# #
# # i = 0
# # while i < len(some_list):
# #     print(some_list[i])
# #     i += 1
#
# # iterator 反復処理をするもの
# for i in some_list:
#     print(i)
#
# for s in 'abcde':
#     print(s)
#
# for word in ['My', 'name', 'is', 'Mike']:
#     if word == 'name':
#         continue    # skipする
#     print(word)
# # My
#
# for word in ['My', 'name', 'is', 'Mike']:
#     if word == 'name':
#         continue    # skipする
#     print(word)
# # My
# # is
# # Mike


###


# for fruit in ['apple', 'banana', 'orange']:
#     print(fruit)
# else:
#     print('I ate all')


# for fruit in ['apple', 'banana', 'orange']:
#     if fruit == 'banana':
#         print("stop eating")
#         break
#     print(fruit)
# else:
#     print('I ate all')


###

# num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# for i in num_list:
#     print(i)
#
# for i in range(10):
#     print(i)
#
# for i in range(2, 10):
#     print(i)
#
# for i in range(2, 10, 3):
#     print(i)
#
# for i in range(10):
#     print(i, 'hello')
#
# # _ の場合, index 不使用
# for _ in range(10):
#     print('hello')


###

# for fruit in ['apple', 'banana', 'orange']:
#     print(i, fruit)
#     i += 1

# for i, fruit in enumerate(['apple', 'banana', 'orange']):
#     print(i, fruit)

###

# days = ['Mon', 'Tue', 'Wed']
# fruits = ['apple', 'banana', 'orange']
# drinks = ['coffee', 'tea', 'beer']
#
# # for i in range(len(days)):
# #     print(days[i], fruits[i], drinks[i])
#
# for day, fruit, drink in zip(days, fruits, drinks):
#     print(day, fruit, drink)

###

# d = {'x': 100, 'y': 200}
#
# for k, v in d.items():
#     print(k, ':', v)
# # x : 100
# # y : 200
#
# print(d.items())
# # dict_items([('x', 100), ('y', 200)])


###

# say_something()

# def say_something():
#     print('Hi')
#
# say_something()
# ## Hi
#
# print(type(say_something))
# ## <class 'function'>

def say_something():
    s = 'hi'
    return s

result = say_something()
print(result)


def what_is_this(color):
    print(color)

what_is_this('red')

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green pepper'
    else:
        return "I don't know"

result = what_is_this('red')
print(result)
result = what_is_this('green')
print(result)
result = what_is_this('yellow')
print(result)



