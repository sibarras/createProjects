#!/bin/bash

function create(){
    cd
    mkdir ~/Desktop/Projects/$1
    python3.8 ~/Desktop/projects/createProjects/mac_create_function/createRepo.py $1
    cd ~/Desktop/Projects/$1
    git init
    touch README.md
    python3.8 -m venv venv
    git add README.md
    git commit -m "first commit"
    git remote add origin https://github.com/sibarras/$1.git
    git push -u origin master
    echo
    echo Repositorio Creado Correctamente 
    echo Repositorio local en en ~/Desktop/Projects/$1
    echo repositorio remoto en https://github.com/sibarras/$1

    code .
    source ./venv/bin/activate
}

#!source automate_creating_projects.sh