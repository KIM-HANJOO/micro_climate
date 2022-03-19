import os
from pathlib import Path

self_module_dir = Path(os.getcwd())
module_dir = self_module_dir.parent
preprocessing_dir = os.path.join(module_dir, 'preprocessing')

target_dir = self_module_dir
target_file = 'polar_to_cartesian.py'

os.chdir(target_dir)
target_file = open(target_file, 'r')
target_string = target_file.read()

crop = target_string

print(target_dir)
print(target_file)
print('\n')
check = 1

while check == 1 :
    try :
        check = 1

        def_pos = crop.index('def')
        end_pos = crop[def_pos :].index(':')
        def_line = crop[def_pos + 4 : def_pos + end_pos]

        crop = crop[def_pos + end_pos + 1 : ]

        print(f'~ {def_line}')
    except :
        break

#print(target_file.read())
        

