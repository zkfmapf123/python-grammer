import os
import subprocess

## Past (Not Recommand)
# os.system('ls')

## Current
subprocess.run(["ls","-al"])
subprocess.run(["pwd"])

## Shell로 실행 (Security issue...) -> Not Recommand
"""
    shell: is execute shell
    check: if occur error -> print error
"""

try:
    subprocess.run("ls -al | grep1 test", shell=True, check=True)
except Exception as err:
    print("err > ", err)

## Principal
## Shell injection을 사용하여 pipe를 피하는 방법 (Command)

p1 = subprocess.Popen(["ls","-al"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(
    ["grep", "test"], stdin=p1.stdout, stdout=subprocess.PIPE
)

p1.stdout.close()
output = p2.communicate()[0]
print(output)
