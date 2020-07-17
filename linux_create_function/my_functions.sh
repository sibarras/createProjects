#!/usr/bin/bash

create(){
    python ~/Desktop/Projects/myConfig/createRepo.py
    cd ~/Desktop/Projects/$1
    source ./venv/bin/activate
    echo
    echo Proyecto creado correctamente
    echo Repositorio remoto en https://github.com/sibarras/$1.git
    echo Repositorio local en /home/sam/Desktop/Projects/$1
}
