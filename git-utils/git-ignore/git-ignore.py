#!/usr/bin/env python3.7
import os
import requests
import sys
# for touch functionality
from pathlib import Path

def display_help():
    """
    Displays the help message
    """
    pass

def main():
    links = {
            'python':'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
            }
    options = [i.lower() for i in sys.argv]
    if len(options) == 1 or options[1] == 'help':
        display_help()
        return
    if options[1] not in links:
        print('Command not recognized. {}'.format(options[1]))
        return

    data = requests.get(links[options[1]]).text
    p = os.getcwd() + '/.gitignore'
    Path(p).touch()
    with open(p,'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
