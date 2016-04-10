#!/bin/bash

./script2.py
./script3.py
python get.py Wikipedista:UrbanecmBot/DisambigLinks | sed -e s/odkazu/odkazů/g > out
./script4.py
python ~/pywikibot/scripts/add_text.py -text:"$(cat out)" -page:"Wikipedista:UrbanecmBot/DisambigLinks"
rm out
