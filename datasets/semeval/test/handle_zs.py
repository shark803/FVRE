#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/24 15:00
# @Author  : Lei Wang
# @File    : handle_zs.py.py
# @Project : FVRE
# @Software: PyCharm


zs_file = "./zs_answer.old.txt"
new_zs_file = "./zs_answer_new.txt"

with open(zs_file,"r") as f, open(new_zs_file,"w") as f2:
    lines = f.readlines()
    for i,line in enumerate(lines):
        line = line.strip()
        if len(line) != 0:
            f2.write(str(8001+i) + "\t" + line + "\n")