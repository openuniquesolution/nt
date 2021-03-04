#!/usr/bin/python3

import argparse
import sys
import os
from datetime import date, time
import subprocess as sp
from jproperties import Properties

def setup():
    propoerty_file = "application.properties"
    config = Properties()
    _dir = os.path.dirname(os.path.abspath(__file__))
    with open(_dir+"/" + propoerty_file, "rb") as _file:
        config.load(_file)
        global extention
        global editor
        global author
        global MAIN_FOLDER_PATH 
        MAIN_FOLDER_PATH = config.get("base.folder").data if(config.get('base.folder') is not None) else "/home/ayushagrawal/notes"
        MAIN_FOLDER_PATH = "/home/ayushagrawal/notes"
        extention = "."+config.get("file_type").data if(config.get('file_type') is not None) else ".md"
        editor = config.get("editor").data if(config.get('editor') is not None) else "vim"
        author = config.get("author").data if(config.get('author') is not None) else ""

def read_args():
    parser = argparse.ArgumentParser()

    subparser = parser.add_subparsers(dest="command")

    find_parser = subparser.add_parser("find", help="find a file in your main application")
    find_parser.add_argument("file_name", help="Name of the file")

    
    save_parser = subparser.add_parser("save", help="save file/s in Git repo of your choice")
    save_parser.add_argument("-m","--message" ,help="Commit messgage for changes")
    save_parser.add_argument("-f","--file", help="specific file you want to commit")

    open_parser = subparser.add_parser("open", help="Open file or create new if not exist.")
    open_parser.add_argument("file_name", help="file name to open")
    open_parser.add_argument("-b", "--book", help="Book for note", default="")
    open_parser.add_argument("-t", "--topic", help="Topic for note", default="")
    open_parser.add_argument("-a", "--author", help="Autor of the document", default="")

    return parser.parse_args()


def find_file(_file):
    _file = _file+extention
    for root, _, files in os.walk(MAIN_FOLDER_PATH):
        if(_file in files):
            print(root + "/" +_file)


def open_file_not_exist(_file, book, topic):
    _dir = MAIN_FOLDER_PATH + "/" + book 
    
    if(not os.path.exists(_dir)):
        os.makedirs(_dir)

    author = parsed.author if(parsed.author != "") else "Ayush Agrawal"
    os.chdir(_dir)
    with open(_file+extention, 'w') as f:
        f.write("Date: " + str(date.today) + "\nAuthor: "+author+"\nBook: " + book + "\nTopic: "+topic + "\n\n\n---\n")

def save_file():
    # git_message = parsed.message if(parsed.message is not None) else "Adding commit"
    pass


def open_file(_file):
    _book = parsed.book
    _topic  = parsed.topic

    file_path = MAIN_FOLDER_PATH + "/" + _book + "/"+_file+extention
    if(not os.path.exists(file_path)):
        open_file_not_exist(_file, _book, _topic)

    sp.call(editor + " " +file_path, shell=True)

def main():
        if(parsed.command == "find"):
            find_file(parsed.file_name)
        if(parsed.command == "open"):
            open_file(parsed.file_name)
        if(parsed.command == 'save'):
            save_file()


parsed = read_args()

if __name__ == "__main__":
    setup()
    main()