from abc import ABC, abstractmethod, ABCMeta


class AbstractParent(ABC):

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError


class Mother:
    def __init__(self, age=0):
        self.age = age
        print('Mother constructor!')

    def do_work(self):
        print("I'm working")

    @staticmethod
    def do_house_work():
        print("listening to music")

    @staticmethod
    def make_father_do_work():
        print("Lazy father do work!!!")
        Father.do_house_work()


class Father(AbstractParent):
    def __init__(self):
        super().__init__()
        print('Father constructor!')

    @staticmethod
    def play_guitar():
        print('play guitar')

    @staticmethod
    def do_house_work():
        print("sitting on the sofa")

    def hello_friend(self):
        pass


class Daughter(Mother, Father):

    def init(self, age=0):
        Mother.__init__(self, age=age)
        Father.__init__(self)

    def do_work(self):
        print("I'm working like a horse!")

    def hello_friend(self):
        pass


class Friend:
    pass


def greet_mother(mother: Mother):
    print("Hello mother!!!")
    mother.do_work()


def greet_father(father: Father):
    print("time to beer!")
    father.play_guitar()


if __name__ == "__main__":
    daughter = Daughter()
    # daughter.__class__ = Friend
    # mother = Daughter()
    # mother.do_work()
    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()

    mother = Mother()
    mother.make_father_do_work()

    for x in [daughter]:
        x.do_house_work()

    # list
    povtorka_list = {"discrete_math", "ukr_mova"}

    # turple
    vasian = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 10, "call"}

    # frozen set
    another_set = frozenset(["di", "ni", "du"])

    # dictionary
    my_dict = {1: "first", "2": 123}
