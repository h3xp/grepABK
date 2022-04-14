#!/bin/python3
# -*- coding: iso-8859-15 -*-
import requests
import argparse
from datetime import date, datetime

MAX_DATES = 4  # define how many dates should get forecasted, 4 looks best, maximum is 9
WASTE = 1  # 1/0 to toggle output for residual waste on/off
PAPER = 1  # 1/0 to toggle output for paper on/off
PLASTIC = 1  # 1/0 to toggle output for plastic on/off

WASTE_COLOR           = "\033[0;35m"
PAPER_COLOR           = "\033[0;34m"
PLASTIC_COLOR         = "\033[0;33m"
WASTE_COLOR_BRIGHT    = "\033[0;95m"
PAPER_COLOR_BRIGHT    = "\033[0;94m"
PLASTIC_COLOR_BRIGHT  = "\033[0;93m"
DEFAULT_COLOR         = "\033[0;39m"
GRAY_COLOR            = "\033[0;35m"

parser = argparse.ArgumentParser(description="grepABK by h3xp",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                 epilog="example usage: python3 grepABK.py Kaistraße 1")
parser.add_argument("street", help="Name of the street.")
parser.add_argument("num", help="Street number of the apartement/house.", type=int)
args = parser.parse_args()

today = date.today()
year = today.strftime("%Y")
street = args.street
num = args.num
if MAX_DATES > 9:
    MAX_DATES = 9

requestURL = "https://www.abki.de/abki-services/leerungen-data?Zeitraum="+year+"&Strasse_input="+street+"&Strasse=13770001&IDSTANDORT_input=%20"+str(num)+"&IDSTANDORT=297416001&Hausnummernwahl=297416001"
r = requests.get(requestURL)
r_dictionary = r.json()


def getdates(tonne_id):
    count = 0
    x = []
    for dates in r_dictionary['termine'][tonne_id]['list']:
        if datetime.strptime(dates['VALUE'].split()[0],'%d.%m.%Y') > datetime.strptime(today.strftime('%d.%m.%Y'),'%d.%m.%Y'):
            if count < MAX_DATES:
                x.append(dates['VALUE'])
                count += 1
            else:
                return x


def print_output(kind, color, color_bright):
    bin_ascii_art = [" _/-\\_", "|-----|", " | | | ", " | | | ", " |___| "]
    date_list = getdates(kind)
    date_list.insert(0, color_bright + " " + r_dictionary['termine'][kind]['titel'] + DEFAULT_COLOR)

    if len(date_list) > len(bin_ascii_art):
        bin_ascii_art.extend(["       "]*(len(date_list)-len(bin_ascii_art)))
    else:
        date_list.extend(["       "]*(len(bin_ascii_art)-len(date_list)))

    for x in range(len(bin_ascii_art)):
        bin_ascii_art[x] = color_bright + bin_ascii_art[x] + DEFAULT_COLOR
    for x in range(len(date_list)):
        date_list[x] = color + date_list[x] + DEFAULT_COLOR
    nice_output = "\n".join("{} {}".format(x, y) for x, y in zip(bin_ascii_art, date_list))
    print("\n"+nice_output)


if WASTE:
    print_output(0, WASTE_COLOR, WASTE_COLOR_BRIGHT)
if PAPER:
    print_output(1, PAPER_COLOR, PAPER_COLOR_BRIGHT)
if PLASTIC:
    print_output(2, PLASTIC_COLOR, PLASTIC_COLOR_BRIGHT)

print("\n"+"\033[90m" + r_dictionary['stand'] + "\033[39m")