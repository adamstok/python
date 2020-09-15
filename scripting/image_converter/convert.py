from PIL import Image
import sys
import os

help_msg =  """
Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP 
Usage:
    python convert.py -a <new_fileformat>  (convert all files in the directory to the desired format)
    python convert.py -r <new_size> (resize image with ex: new_size = 200x300)
    python convert.py -ar <new_size> (resize all images with ex: new_size = 200x300)
    python convert.py <file1> <file2> (convert file1 to file2 )
"""
files = os.listdir(".")
allowed = ['jpeg','png','bmp'] 
arguments = ['-a','-r','-ar']

def check_args():
    listed = [x for x in sys.argv]
    if len(listed)<2:
        return help_msg
    elif listed[1] in arguments or check_files(listed[1]):
        return listed[1:]
    elif  listed[2] in allowed or check_files(listed[2]):
        return listed[1:]
    else:
        return help_msg


    # try:
    #     sys.argv[1],sys.argv[2]
    #     return True
    # except:
    #     print(help_msg)
    #     return False


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
    try:
        Image.open(file).save(new_name)
        print(f'{file} -> {new_name}')
    except:
        print('An error occurred')


# if check_args() == True:
#     if sys.argv[1] == '-a' and sys.argv[2] in allowed:
#         i = 0
#         for f in files:
#             if check_files(f):
#                 convert_file(f, sys.argv[2])
#                 i+=1
#             if i == 0:
#                 print('Nothing to do')
#     elif sys.argv[1] == '-r' and sys.argv[2].split('x')[0].isdecimal() and sys.argv[2].split('x')[-1].isdecimal():

print(check_args())
