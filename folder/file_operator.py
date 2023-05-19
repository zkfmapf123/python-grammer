import os
import pathlib

## Is Exists 
print(os.path.exists("test.txt")) ## is exists file in path
print(os.path.isfile('test.txt')) ## is correct file
print(os.path.isdir('public')) ## is correct folder

## folder
os.makedirs('test_folders')
os.rename('test_folders',"test_folders_2")
os.rename('test_folders_2', 'test_folders')
os.rmdir('test_folders')

## Symbolik linke, Hard link
# os.symlink('reanmed.txt', 'symlink.txt')


pathlib.Path('empty.txt').touch()

