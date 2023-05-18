## class Human(Object)
class Human:
    name: str ## public

    ## 생성자
    def __init__(self, name: str) -> None:
        print("constructor")
        self.name = name
        pass

    def cry(self):
        print("{} is crying".format(self.name))

    def big_cry(self):
        for _ in range(3):
            self.cry()
        else:
            print("i end big_cry")
    
    ## 소멸자
    ## 1. 해당 오브젝트를 더이상 사용하지 않을때
    ## 2. 명시적으로 부를 경우
    def __del__(self):
        print("{} destructor".format(self.name))
        


######################### implementation #########################
leedonggyu, limjeahyock = Human("leedonggyu"), Human("limjeahyock")
leedonggyu.cry()
del leedonggyu

limjeahyock.big_cry()

