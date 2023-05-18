animal = "cat"

def f():
    """
    UnboundLocalError: cannot access local variable 'animal' where it is not associated with a value
    이미 글로벌 변수가 존재 -> 로컬변수의 access 불가능
    """

    print("animal >> ", animal)
    # animal = 'dog' 
    # print("animal >> ", animal)

f()

def global_access_f():
    """
    거의 안쓰겠다.
    """
        
    global animal
    animal = "dog"
    print("global aniaml >> ", animal)

global_access_f()
