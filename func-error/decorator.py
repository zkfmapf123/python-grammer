## not use Decorator
def add_num(a,b):
    return a+b

# print("start")
# print(add_num(10,20))
# print("end")

## use Decorator
def print_info(func):

    ## Decorator
    def decorator_wrapper(*args, **kwargs):
        print("start")
        r = func(*args, **kwargs)
        
        ## 실행결과 => r
        print("end")
        return r
    return decorator_wrapper

@print_info
def min_num(a,b):
    return a-b

print(min_num(10,20))
