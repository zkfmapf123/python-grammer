def write_file(file_name: str, str: str) -> None:
    """
    desc : write file
    """
    _file_name = "./public/{}".format(file_name)
    f = open(_file_name, 'w')
    print("str\n" * 10, sep="##", end="!", file=f)
    f.close()

def read_file(file_name: str) -> None:
    """
    desc : read file
    """
    _file_name = "./public/{}".format(file_name)
    f = open(_file_name, 'r')
    descs = f.readlines()

    for i,desc in enumerate(descs):
        print(i, ">>", desc)

    f.close()

def open_file_use_with(file_name: str) -> None:
    """
        with:
        파일을 open할때는 close를 꼭 해줘야 함 -> 메모리 낭비\n
        with를 사용하면 close를 하지 않아도 됨
    """
    _file_name = "./public/{}".format(file_name)
    with open(_file_name,"w") as f:
        print("hello world" * 10, end="!",file=f)

def write_big_text(file_name: str) -> None:
    """
        desc:
            1. readlines
            2. read(chunk)
    """
    _file_name = "./public/{}".format(file_name)
    chunk = 2

    with open(_file_name) as fs:
        while True:

            ## 1. line read method
            # line = fs.read(chunk)
            # print(line)

            ## 2. line read method
            line = fs.readlines()
            for l in line:
                print(l)

            if not line:
                break
        
def file_seek(file_name = "test.txt") -> None:
    """
        w+ : write + read
    """
    _file_name = "./public/{}".format(file_name)
    # with open(_file_name, "w+") as fs:
    #     fs.write("hello world")
    #     fs.seek(0) ## 처음으로 돌아감
    #     print(fs.read())

    with open(_file_name, "r+") as fs:
        print(fs.read())
        fs.seek(0)
        fs.write("hello world")
        

    


## write_file("test.txt", "hello world")
## read_file("test.txt")
## open_file_use_with("test.txt")
## write_big_text("test.txt")
## file_seek()

