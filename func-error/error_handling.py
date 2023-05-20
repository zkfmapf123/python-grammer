l = [1,2,3]
i = 5

try:
    print(l[i]) ## Error
except:
    print("Not Exists")
finally:
    print("Finally")

## Except Specific Error
try:
    print(l[i])
except IndexError as err:
    print("Index Error : {}".format(err))
except NameError as err:
    print("Name Error : {}".format(err))
finally:
    print("IndexError")

## Exception
try:
    print(l[i])
except Exception as err:
    print("Base Exception : {}".format(err))
else: ## 성공 시
    print("else")
finally:
    print("End")

"""
try:
    시도
except:
    예외 1
except:
    예외 2
except:
    예외 3
else:
    성공 시
finally:
    마지막 
"""

## 독자 예외 (본인만의 Error Class)

class UpperCaseError(Exception):
    pass


def check(words = None):
    if words is None:
        words = ["apple", "ornage", "banana","A"]
    
    for word in words:
        if word.isupper():
            raise UpperCaseError(word)

try:
    check()
except UpperCaseError as err:
    print("This is my fault {}".format(err))

