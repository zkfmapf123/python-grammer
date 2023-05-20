import subprocess

from src.fileio import index as FileIo
from src.interaction import index as Interaction


def register_user(inter : Interaction.Interaction, fileio : FileIo.RobertorIO):
    """
        desc: register user
    """
    profile = {
        "name" : None,
        "age" : None,
        "job" : None
    }

    profile_keys = profile.keys()
    for i,v in enumerate(profile_keys):
        r = inter.user_input("{0} / {1} What is your {2}? ".format(i+1, len(profile_keys), v))
        profile[v] = r

    if not fileio.setting_user_info(profile,profile_keys):
        print("[caution] overlap name!!.")

def find_user(inter: Interaction.Interaction, fileio : FileIo.RobertorIO):
    """
        desc: find user
    """

    user_name = inter.user_input("what find name? ")
    user = fileio.find_user(user_name, ("name", "age", "job"))

    if user is None:
        print("Not Exists")
    else:
        print("""
            name : {}
            age  : {}
            job  : {}
        """.format(user["name"], user["age"], user["job"]))

    inter.user_input("is verify? (press the enter)")

############################################# init #######################################
lookup_table = {
    "1" : register_user,
    "2" : find_user,
    "3" : None,
    "4" : None,
    "5" : None,
    "6" : None,
}


def init() -> None:
    """
        [x] 회원등록 
        [x] 회원찾기
        [x] 서비스 종료
    """
    inter, fileio = Interaction.Interaction(),FileIo.RobertorIO()
    
    count = 1
    while True:
        subprocess.run("clear", check=True)
        print("################ {} ###############".format(count))
        count+=1

        num = inter.user_init_input()
        if num == 9:
            continue

        if num == 0:
            print("bye")
            break
    
        subprocess.run("clear")
        lookup_table.get(str(num))(inter, fileio)
        

init()
