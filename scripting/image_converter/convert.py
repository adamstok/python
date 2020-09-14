from PIL import Image
import sys
import os

help_msg =  "Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP "
files = os.listdir()

def check_files(file):
    allowed = ['jpeg','png','bmp'] 
    file_format = file.split('.')[-1].lower()
    if file_format in allowed:
        return True
    return False








