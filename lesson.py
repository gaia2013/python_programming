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