from src.fileio import index as FileIo
from src.interaction import index as Interaction


def init() -> None:
    """
        1. 회원등록
        2. 회원찾기
        3. 메뉴선택
        4. 메뉴추천
        5. 회원삭제
    """
    inter, fileio = Interaction.Interaction(),FileIo.RobertorIO()
    
    while True:
        init_profile(inter,fileio)

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
        print("이름이 중복됩니다.")

    



    

    
    
    
    


init()
