#!/bin/bash
#MAN is the package manager
MAN=$1

sudo bash ./expect.sh $MAN
sudo bash ./firefox.sh $MAN
sudo bash ./geckodriver.sh $MAN
sudo bash ./pip-selenium.sh $MAN
firefox https://developers.google.com/gmail/api/quickstart/python
echo "Go to: https://developers.google.com/gmail/api/quickstart/python"
echo "Set up your Gmail authentication for automatic notification to the new hire"
