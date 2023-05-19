import os
import pathlib
import shutil
import tarfile

"""
    압축파일 동작
"""

def make_tar_file(folder_name = "tar_example") -> list[str]:

    """
        압축파일할 파일들 생성
    """

    if os.path.exists("{}.tar.gz".format(folder_name)):
        os.remove("{}.tar.gz".format(folder_name))

    if os.path.exists(folder_name):
        shutil.rmtree(folder_name)

    os.mkdir(folder_name)
    files = ["text_1.txt", "text_2.txt","text_3.txt"]
    for file in files:
        pathlib.Path("{}/{}".format(folder_name,file)).touch()

    return ["{}/{}".format(folder_name,file) for file in files]
    

def write_each_file(files: list[str]) -> str:

    """
        파일들 데이터 Write
    """
    for file in files:

        with open(file, 'w+') as f:
            f.write("hello world")

    return files[0].split("/")[0]

def zip_file(folder_name : str) -> None:
    with tarfile.open("{}.tar.gz".format(folder_name),"w:gz") as tf:
        tf.add(folder_name)

    shutil.rmtree(folder_name)

def unzip_file(folder_name: str) -> None:
    
    with tarfile.open("{}.tar.gz".format(folder_name),"r:gz") as tf:
        with tf.extractfile("public/sub_dir/") as f:
            print(f)
        
folder = write_each_file(make_tar_file())

zip_file(folder)
unzip_file(folder)

