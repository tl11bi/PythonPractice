#!/bin/bash

echo "stealing your password and encrypt it"
read -p "Enter API user id: " ID
read -s -p "Enter API password: " PW
echo
echo

PW=$(echo ${PW} | base64)

#Create .flaskenv file
echo "Initializing dotenv file"
cat  <<EOF > .env
# software function
DEBUG=True
VERIFY_REQUEST=False

# user and password, password here are encrypt with 64 bit
USER=${ID}
PASSWORD=${PW}

# directory setup
DATA_DIR=data
LOG_DIR=log
OUTPUT_DIR=output
EOF

echo -e "\n.env created:\n"
echo "installing python environment"
# redhat doesn't come in with pythonvenv installed, install it first before running this code
# yum install python36-devel
# yum install python36-setuptools
# yum install python36-virtualenv

python_path=`which python3`
# $python_path -m venv xlrpvenv
python3 -m virtualenv xlrpvenv

source venv/bin/activate
pip3 install -r requirements.txt
