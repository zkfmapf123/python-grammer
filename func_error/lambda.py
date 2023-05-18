l = ["Mon","tue", "wed","Thu","fri","Sat","sun"]

def change_words(words,func):
    for word in words:
        func(word)

## Not use Lambda
# def change_uppercase(word: str):
#     print(word.upper())

# def change_lowercase(word: str):
#     print(word.lower())

# change_words(l, change_uppercase)
# change_words(l, change_lowercase)

## use Lambda
change_words(l, lambda word: print(word.upper()))
change_words(l, lambda word: print(word.lower()))
