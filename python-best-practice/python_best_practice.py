import subprocess
import time

# 1. Do Not Semicolon

x = 1
y = 1

# 2. maxLength is limit 80

x = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"

# 3. Comment prefix


def test_func(a, b, c,
              asdfasdfasdfasdfaasdfasdaalsdknflasdnfladsfsdlfijasldkfasdffasdfasdfasdfasdfasdfsdf='test'):
    """
       title: title
       desc: desc
       param a: a
       param b: b 
       param c: c 
       return : None

       Node:
            See Details at: http://www.naver.com        
    """
    None


# 4. except "( )"
if x and y:
    print("exists")

# 5. space only 4
if x:
    print("exists")

    x = {
        "test": "sss"
    }

# 6. swap

if x:
    x, y = y, x

# 7. import
# from python_best_practice import (함수자체를 import하지 말아야 함)

# 8. Exception

# Bad Code (do not Exception)


def func():
    try:
        None
    except Exception as err:
        print(err)

# Good Code (raise Exception)


class MainError(Exception):
    pass


def func2():
    raise MainError('error')

# 9. Bad Code (list)


x = [i for i in [1, 2, 3] for x in [1, 2, 3] for y in [1, 2, 3]]

# 10. dictionary

d = {"a": 100, "b": 200, "c": 300}

# k, v not meaning naming (bad code)
for k, v in d.items():
    print(k, v)

# meaning naming (good code)
for alpha, num in d.items():
    print(alpha, num)

# 11. use generator (왠만하면 사용해라)
# generator는 메모리에서 빨리 동작한다 (for 보다)


def t_use_for() -> int:
    """
        desc: 
            use for
    """
    num = 0
    for i in range(10000):
        num += 0
    return num


def t_use_generator() -> list:
    """
        desc:
            use generator
    """
    _num = []
    for i in range(10000):
        yield i


start_time = time.time()
print(t_use_for())
end_time = time.time()
print("use for >> ", end_time - start_time)

start_time = time.time()
_num = 0
for num in t_use_generator():
    _num += num

print(_num)
end_time = time.time()
print("use generator >> ", end_time - start_time)

# 12. use Lambda


def other_func(num: int, cb):
    """
        None
    """
    return cb(num)


def mul_func(x: int) -> int:
    """
        None
    """
    return x * 2


print(other_func(10, mul_func))
print(other_func(10, lambda x: x + 20))

# 13. if else

y = "afsdlkfnasdf"
x = 1 if y else 2  # 스타일마다 다름
print(x)

# 14. Default Parameter


def get_most_popular(self, not_list=None):

    if not_list is None:
        not_list = []


# 15. clojure

def base(x):
    def plus(y):
        return x + y
    return plus


# use clojure -> Decorator에 사용 됨
plus = base(10)
print(plus(20))

# curring
print(base(10)(20))

# Entry Point
# if __name__ == "__main__":
#     main()
