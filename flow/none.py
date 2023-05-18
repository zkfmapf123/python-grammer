is_empty = None ## null, undefined
## print(help(is_empty))

## Check None Condition 1
if is_empty is None:
    print("None")
else:  
    print("Not None")

if is_empty is not None:
    print("Not none")

## Check None Condition 2
if is_empty:
    print("Not None")
else:
    print("None")

print(1 == True)
print(1 != True)
print(1 is True)
print(1 is not True)


