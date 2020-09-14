from PIL import Image
import sys
import os

help_msg =  """
Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP 
Usage:
    python convert.py -a <new_fileformat>  (convert all files in the directory to the desired format)
    python convert.py <file1> <file2> (convert file1 to file2 )
"""
files = os.listdir(".")
allowed = ['jpeg','png','bmp'] 


def check_files(file):
    file_format = file.split('.')[-1].lower()
    if file_format in allowed:
        return True
    return False


def convert_file(file,new_format):
    name = file.split('.')[0]
    new_name = f'{name}.{new_format}'
    Image.open(file).save(new_name)
    print(f'{file} -> {new_name}')


if sys.argv[1] == '-a' and sys.argv[2] in allowed:
    for f in files:
        if check_files(f):
            convert_file(f, sys.argv[2])





