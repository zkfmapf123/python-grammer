class Human(object):
    
    def __init__(self, **kwargs) -> None:
        self._name = kwargs["name"]
        self._age = kwargs["age"]
        self._personaliy = kwargs["personality"]

    def introduce(self):
        print("my name is {0} age {1}. personliay {2}".format(self._name, self._age, self._personaliy))

    ## getter
    @property 
    def name(self):
        return self._name

    ## setter
    @name.setter
    def name(self, name):
        self._name = name

    ## only read
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age
    
    ## only read
    @property
    def personaliy(self):
        return self._personaliy

    @personaliy.setter
    def personaliy(self, personality):
        self._personaliy = personality

man = Human(
    name="leedonggyu",
    age= 30,
    personality="good"
)

man.introduce()

