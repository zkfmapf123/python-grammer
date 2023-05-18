list = [1,2,3,4,5,6,7,8,9,10]
print(list[0])
print(list[1:3])
print(list[:])
print(list[5:])
print(len(list))

n = [1,2,3,4,5,6,7,8,9,10]
print(n[::2])
print(n[::3])
print(n[::-1])

a = ['a','b','c']
b = [1,2,3]
nestedC = [a,b] # [[], []]
print(nestedC)

s = ["a","b","c","d","e","f","g"]
print(s)
s[0] = 'X'
print(s)
s[2:5] = ['C','D','E']
print(s)
s[2:5] = [] # shift 
print(s)
s[:] = []
print(s)

ss = [1,2,3,4,5,6,7,8,9,10]
ss.append(100)
print(ss)
ss.insert(0,200)
print(ss)
ss.pop()
print(ss)

del ss[0] # Caution
print(ss)

del ss # Delete ss (hard link)

nn= [1,2,3,4,5,6,7,8,9,10]
print(nn)
nn.remove(2)
print(nn)
nn.insert(1, 2)
print(nn)

n1 = [1,2,3,4,5]
n2 = [6,7,8,9,10]
x = n1+n2
print(x)

n1 += n2
print(n1)

n2.extend([1,2,3,4,5])
print(n2)

r = [1,2,3,4,5,1,2,3]
print(r.index(3), r.index(3,3))

print(r.count(3))

# method
if 5 in r: 
    print('exists')

r.sort() # sort
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s1 = "My name is Leedonggyu"
to_split = s1.split(" ")
print(to_split)

# copy

## shallow copy
i = [1,2,3,4,5]
j = i

i[0] = 10

print("shallow copy")
print("i : ", i)
print("j : ", j)

## deep copy
i = [1,2,3,4,5]
j = i.copy()

i[0] = 10
print("deep copy")
print("i : ", i)
print("j : ", j)

print(id(i)) ## Adress i 
print(id(j)) ## Adress j

# Example
seat = []
min,max = 0, 5
print(min <= len(seat) < max)
