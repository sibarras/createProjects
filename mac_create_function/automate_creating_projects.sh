#!/bin/bash

function create(){
    cd
    mkdir ~/Desktop/Projects/$1
    python3.8 ~/Desktop/projects/config_folder/createRepo.py $1
    cd ~/Desktop/Projects/$1
    git init
    touch README.md
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/sibarras/$1.git
    git push -u origin master
    # python3.8 -m venv venv
    code .
    # source ./venv/bin/activate
}

#!source automate_creating_projects.sh