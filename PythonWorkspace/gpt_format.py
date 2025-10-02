#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import re
import random
import pyperclip

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")
NOTES_DIR = "F:\\Obsidian\\Notes\\DefaultNotes\\世界\\澳新\\IELTS\\Articles"
VOCABULARY_HEADER = """Here's your vocabulary list for the paleontology-related words. Each entry includes IPA (UK and US), a short explanation (CEFR B2–C2 level with OPAL prioritization where applicable), and 2–3 example sentences."""
VOCABULARY_FOOT = """Would you like this vocabulary set exported as a file (e.g., PDF or Excel), or continue with more words?"""

def main():
    gpt_text = pyperclip.paste()
    output_text = gpt_text
    if gpt_text.find(VOCABULARY_HEADER) >= 0:
        results = re.subn(r"---\r\n\r\n", "", output_text, 0, re.MULTILINE)
        if results[1] > 0:
            output_text = results[0]
        results = re.subn(r"[*]{2}\d+\. (\w+)[*]{2}(.*)", r"## \1\2", output_text, 0, re.MULTILINE)
        if results[1] > 0:
            output_text = results[0]
        output_text = output_text.replace(VOCABULARY_HEADER, "")
        output_text = output_text.replace(VOCABULARY_FOOT, "")
        output_text = output_text.strip("\r\n") + "\n"
    else:
        print("No setting for these text!")
    
    pyperclip.copy(output_text)

if __name__ == "__main__":
    main()
    print("done!")
