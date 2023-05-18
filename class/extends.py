## pass 아무것도 안한다는 뜻
class Animal(object):

    def __init__(self, model=None):
        self.model = model

    def cry(self):
        pass # fallthrough

    def get_tail(self, tail):
        print("tail : {}".format(tail))

class Dog(Animal):

    def __init__(self, model="hosup"):
        super().__init__(model)

    ## override
    def cry(self, sound : str):
        print("{} {}".format(self.model, sound))

######################################## implementation ########################################
hosup = Dog()

hosup.cry("멍멍")
# print(hosup.model)
hosup.get_tail(1)
