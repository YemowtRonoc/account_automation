#!/bin/bash

#MAN is the package manager
MAN=$1

sudo $MAN install python-pip
pip install -U pip
pip install -U google-api-python-client
pip install -U selenium
