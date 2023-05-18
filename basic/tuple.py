# readonly list 
# 읽기전용 list -> 쓰기를 하지 않을 때

t = (1,2,3,4,1,2)
print(t, type(t))
print(t[0])

## t[0] = 10 ## Error

print(t[2:5])
print(t.index(1))

## help(tuple)

## Tuple Unpacking
num_tuple = (10,20)
print(num_tuple)
x,y = num_tuple
print(x, y)
new_tuple = (x,y)
print(new_tuple, type(new_tuple))

a,b = 100, -100
print(type(a), type(b))
b,a = a,b
print(a,b)

# Example
chose_from_two = ('A','B','C')

answer = []
answer.append('A')
answer.append('C')

print(chose_from_two)
print(answer)
