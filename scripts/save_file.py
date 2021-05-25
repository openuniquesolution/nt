
import subprocess as sp
import os

base_dir = os.path.dirname(os.path.realpath(__file__))

def _save_file(_file, message):
    
    sp.call(base_dir+"/../save_file.sh " + MAIN_FOLDER_PATH+" "+_file + " "+ message, shell= True)


def save_file(args, _MAIN_FOLDER_PATH):
    _file = args.file
    _message = args.message
    global MAIN_FOLDER_PATH 
    MAIN_FOLDER_PATH = _MAIN_FOLDER_PATH
    _save_file(
        _file,
        _message
    )
if __name__ == "__main__":
    pass