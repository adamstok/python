from PIL import Image
import sys
import os

def check_newsize(ar):
    try:
        size = ar.split('x')
        if len(size) == 2 and size[0].isdecimal() and size[1].isdecimal():
            return size
        else:
            print(help_msg)
            return False
    except:
        print(help_msg)
        return False


def check_args():
    listed = [x for x in sys.argv]
    if len(listed) <= 2:
        print(help_msg)
        return False
    elif (listed[1] == '-a' and listed[2] in allowed) or (listed[1] == '-ar' and type(check_newsize(listed[2])) == list):
        return listed[1:]
    elif check_files(listed[1]) and check_files(listed[2]):
        return listed[1:]
    else:
        print(help_msg)
        return False


def check_files(file):
    try:
        file_format = file.split('.')[-1].lower()
        if file_format in allowed:
            return True
    except:
        return False

   
def convert_file(file,new_format):
    name = file.split('.')[0]
    new_name = f'{name}.{new_format}'
    if new_name in files:
        print(f'Not converting {new_name}. The file already exist')
        return False
    try:
        Image.open(file).save(new_name)
        print(f'{file} -> {new_name}')
        return True
    except:
        print('An error occurred')
        return False


def resize_files_by_wh(file,new_size):
    pass

def resize_files_by_ratio(file, new_size):
    pass


help_msg =  """
Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP 
Usage:
    python convert.py -a <new_fileformat>  (convert all files in the directory to the desired format)
    python convert.py -r <new_size> (resize image with ex: new_size = 200x300)
    python convert.py -ar <new_size> (resize all images with ex: new_size = 200x300)
    python convert.py <file1> <file2> (convert file1 to file2 )
"""
files = list(filter(lambda x: check_files(x) == True , os.listdir(".")))
allowed = ['jpeg','png','bmp'] 
arguments = ['-a','-r','-ar']


if type(check_args()) == list:
    todo = check_args()
    if todo[0] == '-a' and len(files)>0:
        for f in files:
            convert_file(f,todo[1])
    elif  todo[0] in '-ar' and len(files) == 0:
        print('Nothing to do ! Check the files')


