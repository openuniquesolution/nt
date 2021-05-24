#!/usr/bin/python3

import argparse
import sys
import os
import datetime
import subprocess as sp
import configparser

base_dir = os.path.dirname(os.path.realpath(__file__))

def setup():
    config = configparser.RawConfigParser()
    config.read(base_dir+'/_application.properties')
    details_dict = dict(config.items('SECTION_NAME'))
    return details_dict

def read_args(details_dict):
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    find_parser = subparser.add_parser("find", help="find a file in your main application")
    find_parser.add_argument("-f", "--file_name", help="Name of the file", default="_")
    find_parser.add_argument("-e", "--extention", help="Extention for note", default=details_dict['file_type'])
    find_parser.add_argument("-b", "--book", help="book name for searching all files exist", default="")

    
    save_parser = subparser.add_parser("save", help="save file/s in Git repo of your choice")
    save_parser.add_argument("-m","--message" ,help="Commit messgage for changes", default="Adding new Commit in notes")
    save_parser.add_argument("-f","--file", help="specific file you want to commit", default=".")

    open_parser = subparser.add_parser("open", help="Open file or create new if not exist.")
    open_parser.add_argument("file_name", help="file name to open")
    open_parser.add_argument("-b", "--book", help="Book for note", default="")
    open_parser.add_argument("-e", "--extention", help="Extention for note", default=details_dict['file_type'])
    open_parser.add_argument("-d", "--editor",help="Extention for note", default=details_dict['editor'])
    open_parser.add_argument("-t", "--topic", help="Topic for note", default="")
    open_parser.add_argument("-a", "--author", help="Autor of the document", default=details_dict['author'])
    
    return parser.parse_args()


def find_file(_file, extention, book):

    search_folder  = MAIN_FOLDER_PATH if book == "" else  MAIN_FOLDER_PATH  +"/"+ book 

    _file = _file+"."+extention
    for root, dir, files in os.walk(search_folder):
        if ".git" in dir : 
            dir.remove('.git')
        folder = root.split("/")[-1];
        print(folder)
        if(_file == "_."+extention):
            for inner_file in files:
                print("\t"+ inner_file)
        else:
            if(_file in files):
                print(folder + "\n\t" +_file)


def open_file_not_exist(_file, book, topic, author, extention):
    _dir = MAIN_FOLDER_PATH+ "/" + book 
    
    if(not os.path.exists(_dir)):
        os.makedirs(_dir)

    os.chdir(_dir)
    with open(_file+"."+extention, 'w') as f:
        f.write("Date: " + str(datetime.datetime.now()).split(" ")[0] + "  \nAuthor: "+author+"  \nBook: " + book + "  \nTopic: "+topic + "\n\n\n---\n")

def save_file(_file, message):
    
    sp.call(base_dir+"/save_file.sh " + MAIN_FOLDER_PATH+" "+_file + " "+ message, shell= True)


def open_file(_file, _book, _topic, _author, _extention, editor):
    file_path = MAIN_FOLDER_PATH + "/" + _book + "/"+_file+"."+_extention
    if(not os.path.exists(file_path)):
        open_file_not_exist(_file, _book, _topic,_author,  _extention)

    sp.call(editor + " " +file_path, shell=True)

def main(parsed):
        if(parsed.command == "find"):
            find_file(parsed.file_name, parsed.extention, parsed.book)
        if(parsed.command == "open"):
            open_file(parsed.file_name, parsed.book, parsed.topic, parsed.author, parsed.extention, parsed.editor)
        if(parsed.command == 'save'):
            save_file(
                _file = parsed.file,
                message = parsed.message
            )



if __name__ == "__main__":
    details_dict = setup()
    global MAIN_FOLDER_PATH
    MAIN_FOLDER_PATH = details_dict['base.folder']
    parsed = read_args(details_dict)
    main(parsed)
