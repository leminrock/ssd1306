#!/usr/bin/env python3

import yaml as ya

PATH = 'menu.yaml'

with open(PATH, 'r',encoding='utf-8') as d:
    ydoc = ya.load(d, Loader=ya.FullLoader)

print(ydoc)

def get_pages(di, level=0):
    """get pages"""
    for i in di.items():
        print("pagine:",i[0], "level:", level)
        if isinstance(i[1], dict):
            return get_pages(i[1], level+1)
        else:
            print(i[1])
    return None

print(get_pages(ydoc, 0))