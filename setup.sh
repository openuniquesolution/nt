#!/bin/bash

mkdir ~/.note
cp -r * ~/.note/
cd ~/.note
touch application.properties
echo -e "[SECTION_NAME]" >> application.properties

echo "Provide default extention for file"
read file_type
if [ "${file_type}" == "" ] ; then
    echo "default extention for file required"
    exit
fi
echo -e "file_type=${file_type}" >> application.properties

echo "Provide default editor"
read editor
if [ "${editor}" == "" ] ; then
    echo "default editor required"
    exit
fi
echo -e "editor=$editor" >> application.properties


echo "Provide default base folder"
read base_folder
if [ "${base_folder}" == "" ] ; then
    echo -e "default base folder required\n Please provide full path starting from /home"
    exit
fi
echo -e "base.folder=$base_folder" >> application.properties


echo "Provide default Author"
read author
if [ "${author}" == "" ] ; then
    echo "default editor required"
    exit
fi
echo -e "author=$author" >> application.properties

echo "Provide default Git Url"
read git_url
if [ "${git_url}" == "" ] ; then
    echo "default editor required"
    exit
fi
echo -e "git_url=$git_url" >> application.properties
chmod 777 *
cd
mkdir -p ${base_folder}
cd ${base_folder}
git init
git remote add origin $git_url

echo "alias nt='~/.note/note.py'" >> ~/.bashrc