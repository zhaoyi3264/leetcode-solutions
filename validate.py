#!/usr/bin/python3

import os
import re

ques = re.compile(r'^- \[\d.+')
info = re.compile(r'\[(.+)\]\((src/\d+\.py)\)')

with open('README.md', 'r') as f:
    lines = f.readlines()
    d = len(str(lines))
    for idx, line in enumerate(lines):
        if re.match(ques, line):
            match = re.search(info, line)
            if not match or len(match.groups()) != 2:
                print(f'Line {idx+1:d}: \'{line.strip()}\' format may be incorrect')
                continue
            file = match.group(2)
            if not os.path.exists(file):
                print(f'Line {idx+1:d}: \'{line.strip()}\' file may be missing')
                continue
