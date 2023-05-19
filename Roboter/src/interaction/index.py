class Interaction(object):

    init_cmd = """
        what is your order?
        1. register user
        2. find user

        ## Exit
        0. exit
    """

    def __init__(self) -> None:
        pass

    def __del__(self) -> None:
        pass

    def user_init_input(self, title = init_cmd) -> int:
        """
            desc:
                invalid number code => 7,8\n
                retry_code =>9
        """
        i = int(self.user_input(title))

        if i >= 7 and i <= 9:
            print("Invalid Command")
            return 9
        
        return i

    def user_input(self,title: str) -> str:
        user_input = input(title + "\n" + ">> ")
        return user_input

    