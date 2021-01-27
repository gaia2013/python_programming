# import lesson_package.utils
# from lesson_package import utils
# from lesson_package.utils import say_twice
# from lesson_package.talk import human
# from lesson_package.talk import animal
# from lesson_package.talk import *

# print(animal.sing())
# print(animal.cry())

# r = lesson_package.utils.say_twice('hello')
# r = utils.say_twice('hello')
# r = say_twice('hello')
# r = u.say_twice('hello')

# print(r)

# print(human.sing())
# print(human.cry())

# 新旧パッケージで利用可能にする際に使用
try:
    from lesson_package import utils
except ImportError:
    from lesson_package.tools import utils

utils.say_twice('word')
