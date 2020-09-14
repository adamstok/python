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

def check_files(file):
    allowed = ['jpeg','png','bmp'] 
    file_format = file.split('.')[-1].lower()
    if file_format in allowed:
        return True
    return False

try:
    sys.argv[1]
except:
    print(help_msg)






