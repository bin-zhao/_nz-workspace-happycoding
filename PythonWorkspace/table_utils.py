#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TODO

1. Use dict as basic data structure.
2. Use csv as proto. Save dict as csv.
3. Support translate any other table format to mark down table and reverse.

'''

import sys
import os
import inspect
import re
import random
import pyperclip

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")
NOTES_DIR = "F:\\Obsidian\\Notes\\DefaultNotes\\World\\Australia-NewZealand\\IELTS\\Articles"

def main():
    '''
    output_mode:
        1. GPT prompt.
        2. MD table.
    '''

    source_file_path = ""
    output_mode = 1

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.lexists(file_path):
            source_file_path = os.path.join(ARTICLE_DIR, file_path)
        if not os.path.lexists(source_file_path):
            source_file_path = os.path.join(NOTES_DIR, file_path)
    if len(sys.argv) > 2:
        output_mode = int(sys.argv[2])

    if not os.path.lexists(source_file_path):
        print(f"File {source_file_path} is not exist!")
        return
    if output_mode not in (1, 2, ):
        print(f"Unsupported mode!")
        return

    source_text_file = open(source_file_path, encoding="utf-8")
    source_text = source_text_file.read()
    source_text_file.close()

    word_list = []

    for it_mat in re.finditer(r">([^<]+)</span>", source_text):
        word = it_mat.group(1)
        if word not in word_list:
            word_list.append(word)

    if output_mode == 1:
        word_list_str = '\n'.join(word_list)
        prompt = "Please make a vocabulary for the following word list:\n" + word_list_str
        # print(prompt)
        pyperclip.copy(prompt)
    elif output_mode == 2:
        table_header = "| WORD           | IPA |     |\n| -------------- | --- | --- |\n"
        table_str = table_header + "\n".join([f"| {word} |     |     |" for word in word_list])
        pyperclip.copy(table_str)

    print(f"Total: {len(word_list)}")

if __name__ == "__main__":
    main()
    print("done!")
