count: int = 0

## While
while count < 5:
    print(count)
    count+=1

count: int = 0
while True:
    print("X" * count)
    count+=1

    if count == 10:
        break

## While else (finally 같은 부분)
## 대신 break가 존재할때는 else가 발생하지 않음

## whileElse -> while -> else -> done
## whileElse in break -> while -> done
count: int = 0

while count < 5:
    print(count)
    count+=1

    # break
else:
    print("finally")

## Input 
while True:
    word = input("Enter : ")

    if word == "ok": 
        break
