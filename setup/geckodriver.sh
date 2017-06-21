#!/bin/bash

GECKO=/usr/sbin/geckodriver

if [[ ! -e "$GECKO" ]]; then
    echo "\n\n\n\n TEST PASSED AS TRUE \n\n\n"
    wget https://github.com/mozilla/geckodriver/releases/download/v0.17.0/geckodriver-v0.17.0-linux64.tar.gz
    tar -zxvf geckodriver-v0.17.0-linux64.tar.gz
    sudo mv geckodriver "$GECKO"
    rm -f geckodriver-v0.17.0-linux64.tar.gz
fi
