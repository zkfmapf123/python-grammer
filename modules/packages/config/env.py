try:
    from ..utils import util
except ImportError as err:
    print(err)



def get_db_env() -> dict:
    print("register try-except >> " ,util.get_int())
    
    return {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "root",
        "database_name":"mysql"
    }
