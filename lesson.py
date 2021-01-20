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
