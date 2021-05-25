
import os
import datetime
import subprocess as sp

def open_file_not_exist(_file, book, topic, author, extention):
    _dir = MAIN_FOLDER_PATH+ "/" + book 
    
    if(not os.path.exists(_dir)):
        os.makedirs(_dir)
    os.chdir(_dir)
    with open(_file+"."+extention, 'w') as f:
        f.write("Date: " + str(datetime.datetime.now()).split(" ")[0] + "  \nAuthor: "+author+"  \nBook: " + book + "  \nTopic: "+topic + "\n\n\n---\n")



def _open_file(_file, _book, _topic, _author, _extention, editor):
    file_path = MAIN_FOLDER_PATH + "/" + _book + "/"+_file+"."+_extention
    if(not os.path.exists(file_path)):
        open_file_not_exist(_file, _book, _topic,_author,  _extention)

    sp.call(editor + " " +file_path, shell=True)


def open_file(args, _MAIN_FOLDER_PATH):
    
    global MAIN_FOLDER_PATH
    MAIN_FOLDER_PATH = _MAIN_FOLDER_PATH
    _file = args.file_name
    _book = args.book
    _topic = args.topic
    _author = args.author
    _extention = args.extention
    _editor = args.editor
    _open_file(_file, _book, _topic, _author, _extention, _editor)


if __name__ == "__main__":
    pass