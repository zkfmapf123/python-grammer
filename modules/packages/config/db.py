## 절대경로 (BAD)
# from ..utils import util

from packages.utils import util

## 상대경로 (GOOD)

"""
애스터리스크 -> 별로 좋지는 않으나 파일안에서만 참조할 경우에는 괜찮은 듯
같은 파일에 존재하는 데이터를 참조할때는 __init__로 참조해야 함

__init__.py
>> __all__ = ["env"]
"""
from packages.config import env


def get_database():
    return "mysql", env.get_db_env()

def get_no_db():
    return "mongoDB"

def get_graph_db():
    return "cassandra " , util.get_string()
