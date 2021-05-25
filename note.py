#!/usr/bin/python3

import argparse
import os
import configparser
from scripts.find import find
from scripts.open_file import *
from scripts.save_file import *

base_dir = os.path.dirname(os.path.realpath(__file__))

def setup():
    config = configparser.RawConfigParser()
    config.read(base_dir+'/application.properties')
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






def main(parsed):
        if(parsed.command == "find"):
            find(args=parsed, MAIN_FOLDER_PATH=MAIN_FOLDER_PATH)
        if(parsed.command == "open"):
            open_file(parsed, MAIN_FOLDER_PATH)
        if(parsed.command == 'save'):
            save_file(
                parsed, MAIN_FOLDER_PATH
            )



if __name__ == "__main__":
    details_dict = setup()
    global MAIN_FOLDER_PATH
    MAIN_FOLDER_PATH = details_dict['base.folder']
    parsed = read_args(details_dict)
    main(parsed)
