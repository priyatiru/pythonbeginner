from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir(
    'D:\python\742020') if isfile(join('D:\python\742020', f))]
print(files_list)
