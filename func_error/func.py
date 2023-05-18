## Basic Func
def say_something(str):
    print(str)

say_something("hello")
print(say_something)

func1 = say_something
func1("nono")

def return_say_something(str):
    return str

r = return_say_something("nono111")
print(r)

## Calculator
num: int = 10

def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10,20)
print(r)

r = add_num("a","b")
print(r)

def menu(entree: str, drink : str, dessert: str):
    print(entree, drink, dessert)

## Menu Bad Practice
menu("beaf", "soju", "ice cream")

## Menu Good Practice
menu(entree="stsr", dessert="asdf", drink="123")

## Fixed Parameter
def fixed_menu(entree="beaf", drink="soju", dessert="ice cream"):
    print(entree, drink, dessert)

fixed_menu()
fixed_menu(entree="no beaf", drink="no soju", dessert="no ice cream")

## List는 Default 인수로 사용하면 안된다. -> list는 참조하기 때문에

## Bad Practice
def test_func(x, l = []):
    l.append(x)
    return l

y = [1,2,3]
r1 = test_func(100, y)
print(r1)

y = 123
r2 = test_func(100) ## RunTime Error
print(r2) 

## Good Practie
def test_good_func(x, l = None):
    if l is None:
        l = []

    l.append(x)
    return l

r3 = test_func(100)
r4 = test_func(200)

print(r3)
print(r4)

###################################### 위치인수의 대한 튜플화 (tuple) ######################################
def say_something(word1 = "word1", word2= "word2", word3="word3" ):
    print(word1, word2, word3)

say_something()

### 인수가 몇개 들어오는지 모를때...
def say_something2(*args):
    for arg in args:
        print(">> ",arg)

say_something2("a","b")
say_something2("a","b","c")
say_something2("a","b","c","d")

###################################### 키워드 인수의 사전화 (dict) ######################################
def menu(**kwargs):
    for k, v in kwargs.items():
        print(k, " >> ",v)

menu(entree="beef", drink="soju")

menu_board = {}
menu_board["breakfast"] = "steak"
menu_board["lunch"] = "spagatti"
menu_board["dinner"] = "hungry"
menu(**menu_board)

###################################### tuple + dict ######################################
def hard_menu(food, *args, **kargs):
    print("################")
    print(food)
    
    for arg in args:
        print(arg)

    for k,v in kargs.items():
        print(k,v)
    else:
        print("################")
    
hard_menu("food introduce", "hihi","asdfadf","asdfaf",**{
    "a" : 100,
    "b" : 200,
    "c" : 300
})

##################################### 함수안에 함수 #####################################

### Parameter
def outer(a,b):

    def plus(c,b):
        return c+b

    return plus(a,b)
print(outer(10,20))

### 매개변수안에 함수
def add(a,b): 
    return a+b

def min(a,b):
    return a-b

def outer_func(a,b, func):
    return func(a,b)


print(outer_func(10,20,add))
print(outer_func(10,20,min))

##################################### Clojure #####################################
## 실행지연

def outer(a,b):
    
    def inner():
        return a+b

    return inner

print(outer(1,2)())

