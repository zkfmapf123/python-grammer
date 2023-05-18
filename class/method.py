class Person(object):

    kind = "human"

    ## 생성자
    def __init__(self, **kwargs) -> None:
        self.width = kwargs["width"]
        self.height = kwargs["height"]

    ## 소멸자
    def __del__() -> None:
        pass

    ## 문자열로 사용할때 테스트 용
    def __str__(self) -> str:
        return "World!!!"

    ## 해당 문자열의 대한 길이
    def __len__(self):
        return len(self.text)
    

 
    ## 인스턴스 메서드
    def introduce(self):
        print("I am a {} witdh {}, height {}".format(self.kind, self.width, self.height))

    ## 클래스 메서드
    @classmethod
    def cls_introduce(cls):
        print("I am a {} witdh {}, height {}".format(cls.kind, 0, 0))

    ## 스태틱 메서드
    @staticmethod
    def static_introduce():
        print("hhihihihihihi")

p = Person(
    width=180,
    height=90
)
p.introduce() ## 인스턴스 메서드
p.cls_introduce() ## class method (인스턴스가 만들어지기 전)
Person.static_introduce()


"""

    __eq__
    __ne__
    __lt__
    __gt__
    __le__
    __ge__

    __add__
    __sub__
    __mul__
    __floordiv__
    __truediv__
    __mod__
    __mod__
    __pow__
    __and__
    __or__
"""
