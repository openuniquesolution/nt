#!/bin/bash


base_folder=${1}; shift;
_file=${1}; shift;
message=$@

echo "${base_folder} ${_file}  ${message}"
cd ${base_folder}
pwd
git add ${_file}
git commit -m "${message}"
git push --set-upstream origin master
