#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/12/24 09:41
# @Author  : Lei Wang
# @File    : preprocess.py
# @Project : FVRE
# @Software: PyCharm
import os
import re

# Extract content and remove only the tags
def extract_content_remove_tags(text):
    # Define the regex pattern to find the tags and the content between them
    pattern = r"<(e\d)>(.*?)</\1>"

    # Extract content between tags
    extracted = {match[0]: match[1] for match in re.findall(pattern, text)}

    # Remove only the tags from the text, keep the content
    cleaned_text = re.sub(r"</?e\d>", '', text)

    return extracted, cleaned_text




testfile = "./datasets/semeval/test/test.txt"
prompt_file = "./datasets/semeval/test/prompt.txt"
prompt_template = f"Read the text in the quotes, and choose the most likely answer from the following 19 options below. " \
                  "text: ```{txt}```  " \
                  "(A)  {e2} is caused by {e1}  " \
                  "(B)  {e1} is caused by {e2} " \
                  "(C)  {e2} uses {e1} " \
                  "(D)  {e1} uses {e2}  " \
                  "(E) {e2} manufactures {e1}" \
                  "(F) {e1} manufactures {e2} " \
                  "(G) {e1} is stored in {e2}" \
                  "(H) {e2} is stored in {e1} " \
                  "(I） {e1} is coming or is derived from {e2} " \
                  "(J) {e2} is coming or is derived from {e1} " \
                  "(K) {e1} is moving towards  {e2} " \
                  "(L) {e2} is moving towards  {e1} " \
                  "(M) {e1} is a component of {e2} " \
                  "(N) {e2} is a component of {e1} " \
                  "(O) {e1} forms a nonfunctional part of {e2} " \
                  "(P) {e2} forms a nonfunctional part of {e1} " \
                  "(Q) {e1} is written or spoken about {e2} " \
                  "(R) {e2} is written or spoken about {e1} " \
                  "(S) {e1} and {e2} are not directly related " \
                  "Return the right index, e.g., (A) \n"
prompts = []
with open(testfile,"r") as f, open(prompt_file,"w") as f2:
    test_dataset = f.readlines()
    print(len(test_dataset))
    for line in test_dataset:
        line = line.strip()
        if line.startswith("#"):
            continue
        else:
            contents = line.split("\t")
            txt = contents[1]
            entities, clean_txt = extract_content_remove_tags(txt)
            prompt = prompt_template.format(txt=clean_txt, e1=entities["e1"], e2=entities["e2"])
            #print(prompt)
            prompts.append(prompt)
            f2.write(prompt)

