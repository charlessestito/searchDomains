# searchDomains

This script, given 2 lists of URLs checks to see if there are any matching strings, if so it prints out that URL. The top 10k from 12/14/2015 is given and can be used by making the first file input  =  top10k.csv (as seen in the example)

## Usage
First install publicsuffix
pip install publicsuffix 

To run
./searchDomains.py file1.txt file2.txt

ex. for checking a list(list.txt) with the alexa top 10k: ./searchDomains.py top10k.csv list.txt

