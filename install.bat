@echo off
echo Removing Previous Virtualenv..
rmdir /S /Q wenv
python -m virtualenv wenv
echo Virtualenv Installed. Installing packages..
wenv\scripts\pip install -r requirements.txt