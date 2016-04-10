#!/bin/bash

cd ~/pywikibot
./script2.py
./script3.py
python get.py Wikipedista:UrbanecmBot/DisambigLinks | sed -e s/odkazu/odkazů/g > out
./script4.py
./pwb.py add_text -text:"$(cat out)" -page:"Wikipedista:UrbanecmBot/DisambigLinks"
rm out
