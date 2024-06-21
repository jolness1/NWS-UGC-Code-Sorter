# NWS-UGC-Code-Sorter

## Basics
1) Sorting tool for U.S. National Weather Service UGC codes found here: [NGC Codes NWS](https://www.weather.gov/source/gis/Shapefiles/County/bp05mr24.dbx)

## Prerequisites:
1) Working python3 install (Directions for [Windows](https://kinsta.com/knowledgebase/install-python/#windows)/[Mac](https://kinsta.com/knowledgebase/install-python/#mac)/[Linux](https://kinsta.com/knowledgebase/install-python/#linux)) 

## Usage
1) Naviate to project directory
2) ``python3 nws_script.py``
3) Enter two character state code to filter by state or leave blank to sort all codes
4) Output will be saved in a file ``sorted_codes``

## To Do
1) Filter out the Extraneous data or at least make it more readable
2) Write all entries to db to make it easier to parse and search
3) Move data to it's own file for readability
