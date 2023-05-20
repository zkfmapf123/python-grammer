## 함수의 설명은 안에 써야 함

def example_func(p1, *ps):
    """Example Function with types documented in the docstring.

    Args:
        p1 (int)    : the first params
        ps (...int) : last parameters
    
    Returns
        int : p1 + ...ps
    """

    sum: int = 0 
    for p in ps:
        sum += p
    return p1 + sum


print(example_func.__doc__)
print(example_func(10, 20,30,40,50,60,70,80,90,100))
