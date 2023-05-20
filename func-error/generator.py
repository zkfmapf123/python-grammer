li = ["Good morning", "Good afternoon", "Good night"]

## use For
for l in li:
    print(l)

## use Generator
def greeting():
    yield 'Good morning'
    ## other job
    yield 'Good afternoon'
    ## other job
    yield 'Good night'
    ## other job

# for g in greeting():
#     print(g)

g = greeting()
print(next(g))
print(next(g))
print(next(g))
