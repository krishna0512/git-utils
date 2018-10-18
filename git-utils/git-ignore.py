#!/usr/bin/env python3.7
import os
import requests
import sys
# for touch functionality
from pathlib import Path

def main():
    links = {
            'python':'https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore'
            }
    if sys.argv[1] not in links:
        print('Command not recognized. {}'.format(sys.argv[1]))
    data = requests.get(links[sys.argv[1]]).text
    p = os.getcwd() + '/.gitignore'
    Path(p).touch()
    with open(p,'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
