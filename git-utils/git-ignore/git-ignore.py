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

def load_links():
    p = Path(__file__).resolve().parent
    p = p / 'data'
    p = p.resolve()
    a = os.listdir(str(p))
    return {i.lower().strip().split('.')[0]:(p / i).resolve() for i in a if 'gitignore' in i}

def main():
    options = [i.lower() for i in sys.argv]
    if len(options) == 1 or options[1] == 'help':
        display_help()
        return
    links = load_links()
    if options[1] not in links:
        print('Command not recognized. {}'.format(options[1]))
        return

    with links[options[1]].open() as f:
        r = f.readlines()
    r = [i.strip() for i in r]
    data = '\n'.join(r) + '\n'
    p = os.getcwd() + '/.gitignore'
    if os.path.exists(p):
        os.remove(p)
    Path(p).touch()
    with open(p,'w') as f:
        f.write(data)

if __name__ == '__main__':
    main()
