import os

def find_empty_dir(dir_name):
    empty_dirs = []  
    files_per_directory = {}  

    for dirpath, dirnames, files in os.walk(dir_name):
        directory_name = dirpath.split('/')[-1]
        
        if empty(files):            
            if directory_name != '':
                empty_dirs.append(directory_name)          
        else:
            files_per_directory[directory_name] = len(files)

    return {'files_per_directory': files_per_directory, 
            'empty_directories': empty_dirs}
    
def empty(files):
    return len(files) == 0

#import code; code.interact(local=dict(globals(), **locals()))
