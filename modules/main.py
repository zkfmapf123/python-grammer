from packages.config import db
from packages.utils import util

print(util.get_string(), util.get_int())
print(db.get_database(), db.get_no_db())
print(db.get_graph_db())
