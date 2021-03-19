#!/bin/sh
VENV_PATH="/Users/djoye/Piscine_DS/day03/ex02/djoye"

if [[ -z "$VIRTUAL_ENV" ]]; then
    echo "virtual environment not found"
elif [ $VIRTUAL_ENV != $VENV_PATH ]; then
    echo "incorrect virtual environment"
else
    pip3 install bs4 PyTest
    pip freeze > requirements.txt 
fi
