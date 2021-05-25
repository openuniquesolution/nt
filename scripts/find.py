import os

def printAllBooks():
    for root, dir, files in os.walk(SEARCH_FOLDER):
        if ".git" in dir : 
            dir.remove('.git')
        folder = root.split("/")[-1];
        print(folder)
        for inner_file in files:
            print("\t"+ inner_file)


def find_file(_file, extention):
    _file = _file+"."+extention
    for root, dir, files in os.walk(SEARCH_FOLDER):
        folder = root.split("/")[-1];
        print(folder)
        if(_file in files):
            print(folder + "\n\t" +_file)

def find(args, MAIN_FOLDER_PATH):
    file_name = args.file_name
    extention = args.extention
    book = args.book
    global SEARCH_FOLDER
    SEARCH_FOLDER = MAIN_FOLDER_PATH if book == "" else MAIN_FOLDER_PATH + "/" + book
    
    if(file_name == "_"):
        printAllBooks()
    else:
        find_file(_file=file_name, extention=extention)

    

if __name__ == "__mian__":
    pass