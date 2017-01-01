#!/bin/bash

./script2.py
./script3.py
python get.py Wikipedista:UrbanecmBot/DisambigLinks | sed -e s/odkazu/odkazů/g > out
./script4.py
python ~/pywikibot/scripts/add_text.py -always -text:"$(cat out)" -page:"Wikipedie:Seznam nejvíce odkazovaných rozcestníků/Odkazy"
rm out
