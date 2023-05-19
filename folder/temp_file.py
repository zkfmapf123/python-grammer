import tempfile

"""
    일시적인 파일이기 때문에,
    Runtime이 종료되면 알아서 꺼짐
"""

with tempfile.TemporaryFile(mode='w+') as t:
    t.write("hello")
    t.seek(0)
    print(t.read())

# with tempfile.NamedTemporaryFile(delete=False) as t:
#     with open(t.name, "w+") as f:
        
