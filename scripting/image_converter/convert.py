from PIL import Image
import sys
import os
from pydub import AudioSegment

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
    elif check_input_files(listed[1]) and (listed[2] in allowed_output or listed[2] in music_formats):
        return listed[1:]
    elif len(listed) == 4 and listed[1] == '-r' and check_input_files(listed[2]) and check_newsize(listed[3]):
        return listed[1:]
    elif len(listed) == 3 and listed[1] == '-am' and listed[2] in music_formats:
        return listed[1:]
    else:
        print(help_msg)
        return False


def check_input_files(file):
    try:
        file_format = file.split('.')[-1].lower()
        if file_format in allowed or file_format in music_formats:
            return True
    except:
        return False

   
def convert_file(file,new_format):
    name = file.split('.')[0]
    new_name = f'{name}.{new_format}'
    if new_name in os.listdir('.'):
        print(f'Not converting {new_name}. The file already exist')
        return False
    elif file.split('.')[-1] in allowed and new_format in allowed_output:
        try:
            Image.open(file).save(new_name)
            print(f'{file} -> {new_name}')
            return True
        except:
            print('An error occurred')
            return False
    elif file.split('.')[-1] in music_formats and new_format in music_formats:
        f_format = file.split('.')[-1]
        if f_format == 'wav':
            try:
                # sound = AudioSegment.from_mp3(file)
                # sound = AudioSegment.export(new_name, format="wav")
                # print(f'{file} -> {new_name}')
                sound = AudioSegment.from_file(file,format='mp3').export(new_name,format='wav')
                print(f'{file} -> {new_name}')

            except:
                print('mp3 to wav ERROR')
        else:
            try:
                # sound = AudioSegment.from_wav(file)
                # sound = AudioSegment.export(new_name, format="mp3")
                # print(f'{file} -> {new_name}')
                sound = AudioSegment.from_file(file,format='wav').export(new_name,format='mp3')
                print(f'{file} -> {new_name}')

            except:
                print('wav to mp3 ERROR')



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



def convert_music(f_format):
    music_files = [x for x in list(filter(lambda x: x.split('.')[-1] in music_formats, os.listdir('.'))) if x.split('.')[-1] != f_format]
    if len(music_files) == 0:
        print('Nothing to do ! Check the files')
        return False
    else:
        for song in music_files:
            name = song.split('.')[0]
            dst = f'converted_{name}.{f_format}'
            if f_format == 'wav':
                name = name + '.wav'
                try:
                    # sound = AudioSegment.from_mp3(song)
                    # sound = AudioSegment.export(dst, format="wav")
                    sound = AudioSegment.from_file(song,format='mp3').export(name,format='wav')
                    print(f'{song} -> {name}')
                except:
                    print('mp3 to wav ERROR')
            else:
                name = name + '.mp3'
                try:
                    # sound = AudioSegment.from_wav(song)
                    # sound = AudioSegment.export(dst, format="mp3")
                    print(f'{song} -> {name}')
                    sound = AudioSegment.from_file(song,format='wav').export(name,format='mp3')
                except:
                    print('wav to mp3 ERROR')




help_msg =  """
Allowed files conversions: JPEG, PNG, BMP <=> JPEG, PNG, BMP 
Usage:
    python convert.py -ai <new_fileformat>  (convert all files in the directory to the desired format)
    python convert.py -am <new_fileformat> (convert all music files in the current directory)
    python convert.py -ap  (convert all imgages to one pdf)
    python convert.py -ar <new_size> (resize all images with ex: new_size = 200x300 or ex: 0.5 in case of ratio)
    python convert.py -r <file> <new_size> (resize image with ex: new_size = 200x300, or 0.5 for the ratio)
    python convert.py <file1> <file_format> (convert file1 to formatted file1 )
"""
# TODO: options: convert music, docs - excel, PDF file -> make it smaller 
music_formats = ['wav','mp3']
allowed = ['jpeg','png','bmp'] 
allowed_output = ['jpeg','png','bmp','pdf'] 
arguments = ['-ai','-r','-am','-ap','-ar']
files = list(filter(lambda x: check_input_files(x), os.listdir('.')))
musicfiles = list(filter(lambda x: x.split('.')[-1] in music_formats, os.listdir('.')))

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
    elif check_input_files(todo[0]) and (todo[1] in allowed_output or todo[1] in music_formats):
        convert_file(todo[0],todo[1])
    elif todo[0] == '-r':
        try:
            new_size = tuple([int(x) for x in check_args()[-1].split('x')])
            resize_files_by_wh(todo[1],new_size)
        except:
            new_size = float(check_args()[-1])
            resize_files_by_ratio(todo[1],new_size)
    elif todo[0] == '-am' and len(musicfiles) > 0:
        convert_music(todo[-1])
    elif todo[0] == '-am' and len(musicfiles) == 0:
        print('No music files detected. Check your files!')
    
    # TODO: first if should be checking the len(files)
print(check_args())
