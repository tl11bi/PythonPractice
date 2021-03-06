#!/bin/bash

#Create settings.ini file
cat  <<EOF > settings.ini
[general]
loglevel = INFO

[ldap]
url = ldap://tdbfg.com:3268
user = xxxxxx
password = xxxxxx

[dply1_data]
url =
prefix = DPLY1_accounts_
user = xxxxxx
password = xxxxxx

[cdae1_data]
user = xxxxxx
password = xxxxxx

[local_file]
diamond = CDAE1_01_accounts.xml
platform = CDAE1_config.xml

[nexus_platform]
##
user = xxxxxx
password = xxxxxx
EOF


echo .env created: Initialize credentials before using app!