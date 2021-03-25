# -----------------------------------------------------------------------------
# Name:        aggregator.py
# Purpose:     CS 21A - implement a simple general purpose aggregator
#
# Author:      Jessica Sendejo
# -----------------------------------------------------------------------------
"""
Implement a simple general purpose aggregator
 
Usage: aggregator.py filename topic
filename: input  file that contains a list of the online sources (urls).
topic:  topic to be researched and reported on
"""

import urllib.request
import urllib.error
import re
import sys

def url_data(keyword, urls_dict, filename):
    """Gets all url data from file to urls_arr."""
    with open(filename, 'r', encoding='utf-8') as file:
        for url in file:
            url = url.rstrip()
            res = urllib.request.urlopen(url).read().decode('utf-8')
            search = re.search('<(.*' + keyword + '.*)>', res)
            if(search != None):
                print("[+] " + keyword + " found in " + url)
                urls_dict[url] = search.group(1)
            else:
                print("[-] " + keyword + " not found in " + url)


def write_dict(dict, key):
    """Writes data from dict to a file."""
    file = key + "summary.txt"
    with open(file, 'w', encoding='utf-8') as output_file:
        for keyword in dict:
            output_file.write(key + " " + dict[keyword] + "\n")


def main():
    urls = {}

    try:
        url_data(sys.argv[2], urls, sys.argv[1])
    except IndexError:
        print("Usage: aggregator.py <source file> <keyword>")
        sys.exit(1)
    write_dict(urls, sys.argv[2])

if __name__ == "__main__":
    main()