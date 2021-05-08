# __Notes Taking__  

This application help you to centeralize your notes taking  and maintain them in a git repository system. You can use any git repository website (like Github, Bigbucket) and take tool in any format (like text, md, adoc).

This gives you a power to search, create and open your notes using command line, for editing you can use any editor that can be open using comman line(Like: Vim, Gedit, code)   


---   

There are three mode for this application 

1. Save 
2. Open  
3. Find  

---  
## __Use Cases__   


usage: note.py [-h] {find,save,open} ...   

positional arguments:   

{find,save,open}  


    find            find a file in your main application   
    save            save file/s in Git repo of your choice   
    open            Open file or create new if not exist.   

optional arguments:  


    -h, --help        show this help message and exit  

---  
### __Find Command arguments__   

usage: note.py find [-h] file_name   

positional arguments:  

    file_name   Name of the file  

---   
### __Open Command Argument__  

usage: note.py open [-h] [-b BOOK] [-t TOPIC] [-a AUTHOR] file_name

positional arguments:

    file_name             file name to open

optional arguments:

    -h, --help            show this help message and exit
    -b BOOK, --book BOOK  Book for note
    -t TOPIC, --topic TOPIC
                          Topic for note
    -a AUTHOR, --author AUTHOR
                          Autor of the document
---    
### __Save Command Argument__   

usage: note.py save [-h] [-m MESSAGE] [-f FILE]

optional arguments:

    -h, --help            show this help message and exit
    -m MESSAGE, --message MESSAGE
                          Commit messgage for changes
    -f FILE, --file FILE  specific file you want to commit