# grepABK

## Description

I wrote this script because the garbace containers in front of my appartement are always full and I am always too slow to realize that they got cleared. The script only pulls the data from the API of Abfallwirtschaftsbetrieb Kiel (ABK) hence the name. You could of course do that by hand, but that was too tedious and I also didn't want to clutter my calendar with their iCal-file.

## Usage

Just run:


```
python3 grepABK.py [streetname] [house number]
```


Example:
```
python3 grepABK.py Kaistraße 1
```

## Demonstration

![Screenshot displaying a demonstration of the executed script](screenshot.PNG)

## Help

```
$ python3 grepABK.py --help
usage: grepABK.py [-h] street num

grepABK by h3xp

positional arguments:
  street      Name of the street.
  num         Street number of the apartement/house.

optional arguments:
  -h, --help  show this help message and exit

example usage: python3 grepABK.py Kaistraße 1
```

## Disclaimer

I am in no way affiliated with ABK, this project is for educational purposes only.