from PIL import Image
import sys
import os

def check_newsize(ar):
    try:
        size =  ar.split('x')
        if len(size) == 2 and size[0].isdecimal() and size[1].isdecimal():
            return [int(x) for x in size]
        else:
            try:
                if float(ar):
                    return list(ar)
            except:
                print(help_msg)
                return False
    except:
        print(help_msg)
        return False



def check_args():
    listed = [x for x in sys.argv]
    if len(listed) == 2 and listed[1] == '-ap':
        return ['-ap']
    elif len(listed) >=2 and listed[1] == '-ap':
        print(help_msg)
        return False
    elif len(listed) <= 2:
        print(help_msg)
        return False
    elif (listed[1] == '-ai' and listed[2] in allowed) or (listed[1] == '-ar' and type(check_newsize(listed[2])) == list):
        return listed[1:]
    elif check_input_files(listed[1]) and listed[2] in allowed_output:
        return listed[1:]
    elif len(listed) == 4 and listed[1] == '-r' and check_input_files(listed[2]) and check_newsize(listed[3]):
        return listed[1:]
    else:
        print(help_msg)
        return False


def check_input_files(file):
    try:
        file_format = file.split('.')[-1].lower()
        if file_format in allowed:
            return True
    except:
        return False

   
def convert_file(file,new_format):
    name = file.split('.')[0]
    new_name = f'{name}.{new_format}'
    if new_name in os.listdir('.'):
        print(f'Not converting {new_name}. The file already exist')
        return False
    try:
        Image.open(file).save(new_name)
        print(f'{file} -> {new_name}')
        return True
    except:
        print('An error occurred')
        return False


def convert_to_pdf(file_name,files_list):
    if file_name in os.listdir('.'):
        print(f'Not converting - The file already exist')
        return False
    try:
        img = files_list[0]
        img.save(file_name,'pdf', resolution=100.0, save_all=True, append_images=files_list)
        print(f'{file_name} saved')
        return True
    except:
        print('An error occurred')
        return False


def resize_files_by_wh(file,new_size):
    new_name = f'resized_{file}'
    file_format = file.split('.')[-1]
    if new_name in files:
        print(f'Not converting {new_name}. The file already exist')
        return False
    try:
        img = Image.open(file)
        resized_img = img.resize(new_size)
        resized_img.save(new_name, file_format, optimize=True)
        print(f'{file} -> {new_name}')
        return True
    except:
        print('An error occurred')
        return False



def resize_files_by_ratio(file, new_size):
    new_name = f'resized_{file}'
    file_format = file.split('.')[-1]
    if new_name in files:
        print(f'Not converting {new_name}. The file already exist')
        return False
    try:
        img = Image.open(file)
        width, height = img.size
        width = width * new_size
        height = height * new_size
        resized_img = img.resize((int(width),int(height)))
        resized_img.save(new_name, file_format, optimize=True)
        print(f'{file} -> {new_name}')
        return True
    except:
        print('An error occurred')
        return False


help_msg =  """
Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP 
Usage:
    python convert.py -ai <new_fileformat>  (convert all files in the directory to the desired format)
    python convert.py -ap  (convert all imgages to one pdf)
    python convert.py -ar <new_size> (resize all images with ex: new_size = 200x300 or ex: 0.5 in case of ratio)
    python convert.py -r <file> <new_size> (resize image with ex: new_size = 200x300, or 0.5 for the ratio)
    python convert.py <file1> <file_format> (convert file1 to formatted file1 )
"""
# TODO: options: -r file ratio, convert music, docs - excel

allowed = ['jpeg','png','bmp'] 
allowed_output = ['jpeg','png','bmp','pdf'] 
arguments = ['-ai','-r','-ap','-ar']
files = list(filter(lambda x: check_input_files(x), os.listdir('.')))

if type(check_args()) == list:
    todo = check_args()
    if todo[0] == '-ai' and len(files)>0:
        for f in files:
            convert_file(f,todo[1])
    elif  todo[0] == '-ar' and len(files) == 0:
        print('Nothing to do ! Check the files')
    elif todo[0] == '-ar' and len(files)>0:
        try:
            new_size = tuple([int(x) for x in check_args()[-1].split('x')])
            for f in files:
                resize_files_by_wh(f,new_size)
        except:
            new_size = float(check_args()[-1])
            for f in files:
                resize_files_by_ratio(f,new_size)
    elif todo[0] == '-ap' and len(files) > 0:
        files_list = list(map(lambda x: Image.open(x) ,files))
        file_name = files[0].split('.')[0]+'.pdf'
        convert_to_pdf(file_name,files_list)
    elif todo[0] == '-ap' and len(files) == 0:
        print('No files detected')
    elif check_input_files(todo[0]) and todo[1] in allowed_output:
        convert_file(todo[0],todo[1])
    elif todo[0] == '-r':
        try:
            new_size = tuple(todo[-1].split('x'))
            resize_files_by_wh(todo[1],new_size)
        except:
            new_size = float(check_args()[-1])
            resize_files_by_ratio(todo[1],new_size)

    # TODO: first if should be checking the len(files)

