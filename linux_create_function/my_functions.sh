#!/usr/bin/bash

create(){
    python ~/Desktop/Projects/createProjects/linux_create_function/createRepo.py $1
    echo
    cd ~/Desktop/Projects/$1
    source ./venv/bin/activate
}
