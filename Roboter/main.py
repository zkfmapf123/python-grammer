import subprocess

from src.fileio import index as FileIo
from src.interaction import index as Interaction


def init_profile(inter : Interaction.Interaction, fileio : FileIo.RobertorIO):
    """
        desc: user setting
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

    

lookup_table = {
    "1" : init_profile,
    "2" : None,
    "3" : None,
    "3" : None,
    "4" : None,
    "5" : None,
    "6" : None,
}


def init() -> None:
    """
        [x] 회원등록 
        [ ] 회원찾기

        [ ] Login
        [ ] 메뉴선택
        [ ] 메뉴추천
        [ ] 회원삭제
        [x] 서비스 종료
    """
    inter, fileio = Interaction.Interaction(),FileIo.RobertorIO()
    
    count = 1
    while True:
        subprocess.run("clear")
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
