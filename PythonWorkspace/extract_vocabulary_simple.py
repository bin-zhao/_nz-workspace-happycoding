#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
TODO

1. Save vocabulary for each article.
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
DB_FILE = os.path.join(CUR_DIR, "Assets/Vocabulary.db")

def main():
    '''
    python extract_vocabulary_simple.py output_mode update_vocabulary_db

    output_mode:
        1. GPT prompt. (Default)
        2. MD table.
    
    update_vocabulary_db
        0: False (Default)
        !0: True
        
    '''

    source_file_path = ""
    output_mode = 1
    update_vocabulary_db = False

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.lexists(file_path):
            source_file_path = os.path.join(ARTICLE_DIR, file_path)
        if not os.path.lexists(source_file_path):
            source_file_path = os.path.join(NOTES_DIR, file_path)
    if len(sys.argv) > 2:
        output_mode = int(sys.argv[2])
    if len(sys.argv) > 3:
        update_vocabulary_db = not(int(sys.argv[3]) == 0)

    if not os.path.lexists(source_file_path):
        print(f"File {source_file_path} is not exist!")
        return
    if output_mode not in (1, 2, ):
        print(f"Unsupported mode!")
        return
    
    if update_vocabulary_db:
        vocabulary_db_file = open(DB_FILE, "r+")
        vocabulary_db = [it.strip() for it in vocabulary_db_file.readlines()]
        vocabulary_db_size = len(vocabulary_db)
        vocabulary_db_file.close()

    source_text_file = open(source_file_path, encoding="utf-8")
    source_text = source_text_file.read()
    source_text_file.close()

    word_list = []

    for it_mat in re.finditer(r">([^<]+)</span>", source_text):
        word = it_mat.group(1).strip().capitalize()
        if word not in word_list:
            if update_vocabulary_db:
                if word not in vocabulary_db:
                    word_list.append(word)
                    vocabulary_db.append(word)
            else:
                word_list.append(word)

    if update_vocabulary_db and len(vocabulary_db) != vocabulary_db_size:
        vocabulary_db_file = open(DB_FILE, "w")
        vocabulary_db_file.writelines([f"{it}\n" for it in vocabulary_db])
        vocabulary_db_file.close()
        print("Vocabulary updated!")

    if output_mode == 1:
        word_list_str = '\n'.join(word_list)
        prompt = "Please make a vocabulary for the following word list:\n" + word_list_str
        # print(prompt)
        pyperclip.copy(prompt)
    elif output_mode == 2:
        table_header = "| WORD           | IPA |     |\n| -------------- | --- | --- | --- |\n"
        table_str = table_header + "\n".join([f"| {word} |     |     |     |" for word in word_list])
        table_str += f"\n\n*Vocabulary Size: {len(word_list)}*"
        pyperclip.copy(table_str)

    print(f"Vocabulary Size: {len(word_list)}")

if __name__ == "__main__":
    main()
    print("done!")
