import sys

## python command.py hello world
for i, v in enumerate(sys.argv):
    if i != 0:
        print(v)
