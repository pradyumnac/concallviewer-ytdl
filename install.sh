echo "Removing Previous Virtualenv.."
rm -fR lenv
python -m virtualenv lenv
echo Virtualenv Installed. Installing packages..
lenv/bin/pip install -r requirements.txt
