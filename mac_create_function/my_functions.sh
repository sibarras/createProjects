#!/usr/bin/bash

create(){
    cd ~/Desktop/Projects/createProjects/mac_create_function/
    python3 createRepo.py $1 $2 $3
    echo
    cd ~/Desktop/Projects/$1
    if [ $2 = '-pyenv' ] || [ $3 = '-pyenv' ]
    then
        source ./venv/bin/activate
    fi
}
