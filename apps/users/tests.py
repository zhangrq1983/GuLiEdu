from django.test import TestCase
from random import choice
from random import randrange, randint

# Create your tests here.


def get_random_code(code_length):
    code_source = '2134567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    code = ''
    for i in range(code_length):
        # 随机选择一个字符
        # a = randrange(0, len(code_source))
        # print(a)
        # str = code_source[a]
        # code += str

        a = choice(code_source)
        print(a)
        code += a
    return code


if __name__ == '__main__':
    a = get_random_code(20)
    print(a)

