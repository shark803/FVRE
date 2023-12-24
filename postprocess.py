#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/24 09:42
# @Author  : Lei Wang
# @File    : postprocess.py
# @Project : FVRE
# @Software: PyCharm


import re
zeroshot_answer_file = "./datasets/semeval/test/zs_answer_new.txt"
formal_answer_file = "./datasets/semeval/test/test_answer.txt"

def extract_bracketed_indices(text):
    # Regex pattern to match letters within parentheses
    pattern = r"\([A-Z]\)"

    # Find all matches in the text
    matches = re.findall(pattern, text)

    return matches

label2id_dict = dict()
id2label_dict = dict()
with open("./datasets/semeval/test/label2id.txt","r") as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        label, id = line.split("\t")
        label2id_dict[label] = id
        id2label_dict[id] = label

with open(zeroshot_answer_file,"r") as f, open(formal_answer_file,"w") as f2:
    lines = f.readlines()
    for i,line in enumerate(lines):
        line = line.strip()
        sent_id, answer = line.split("\t")
        answer_id = extract_bracketed_indices(answer)[0]
        #print(str(i)+":"+answer_id)
        label = id2label_dict[answer_id]
        f2.write(sent_id + "\t" + label + "\n")
