#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import re
import random

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")

def main():
    txt_file_path = os.path.join(ARTICLE_DIR, "Temp.txt")
    txt_file = open(txt_file_path)
    lines = txt_file.readlines()
    txt_file.close()

    new_lines = []
    for line in lines:
        new_lines.append("## " + line.capitalize() + "\n")
        new_lines.append("**IPA:** \n\n\n\n")
        # new_lines.append("**Explanation:** \n\n")
        # new_lines.append("**Examples:**\n\n")
        # new_lines.append("1. \n\n")
    
    output_file_path = os.path.join(ARTICLE_DIR, "Temp-out.txt")
    output_file = open(output_file_path, "w")
    output_file.writelines(new_lines)
    output_file.close()

if __name__ == "__main__":
    main()
    print("done!")
