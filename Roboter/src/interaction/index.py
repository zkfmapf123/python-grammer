class Interaction(object):

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    def user_input(self,title: str) -> str:
        user_input = input(title + "\n" + ">> ")
        return user_input
