############################################################################ 리스트 표기 ###############################################################################################
t = (1,2,3,4,5)

## Basic list
r = []
for i in t:
    r.append(i)

print(r)

## use Short list
## i for i in t
## -> 1. for i in t -> 기존 for문이고
## -> 2. 해당 구문을 i로 
r = [i+10 for i in t]
print(r)

## use if

rr = []
for i in t:
    if i % 2 ==0:
        rr.append(i*2)
        continue 

    rr.append(i*3)

print(rr)

## 간단표기만 가능한듯
rr = [i for i in t if i % 2 ==0]


t2 = (5,6,7,8,9,10)
rrr = []
for i in t2:
    for j in t:
        rrr.append(i*j)
    
print(rrr)

## 근데 저렇게 사용하면 가독성이 너무 떨어질듯... 

############################################################################ 사전 표기 ###############################################################################################

w = ["mon","tue","wed"]
f = ["coffe", "milk","water"]

d = {}

for x, y in zip(w,f):
    d[x] = y

print(d)

############################################################################ 집합 표기 ###############################################################################################

s = set()
for i in range(0,10):
    s.add(i)

s = {i for i in range(0,10)}
print(s)
