#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyperclip
import chardet
import sys
import os

NOTE_ROOT = "F:\\Obsidian\\Notes\\DefaultNotes"

def main():
    title = ""
    path = ""

    # if len(sys.argv) > 0:
    #     title = sys.argv[1] + ".md"
    # if len(sys.argv) > 1:
    #     path = sys.argv[2]
    if len(sys.argv) > 0:
        target_path = sys.argv[1] + ".md"
        path, title = os.path.split(target_path)

    if len(title) <= 0 or len(path) <= 0:
        print("need title and path!")
        return

    # print(title, path)
    # return

    full_path = os.path.join(NOTE_ROOT, path, title)
    dir_path = os.path.dirname(full_path)
    append_mode = False

    try:
        if not os.path.lexists(dir_path):
            os.makedirs(dir_path)
    except Exception as ex:
        print(ex)
        #treat as critical error.
        return
    
    if os.path.lexists(full_path):
        # print("note file is exist!")
        append_mode = True
    
    last_item = pyperclip.paste()
    # print(chardet.detect(last_item))
    # last_item = last_item.decode("")
    last_item = last_item.replace("\\[", "$$")
    last_item = last_item.replace("\\]", "$$")
    last_item = last_item.replace("\\( ", "$")
    last_item = last_item.replace(" \\)", "$")
    last_item = last_item.replace("\\(", "$")
    last_item = last_item.replace("\\)", "$")
    last_item = last_item.replace("）**", "）** ")  # TODO
    if append_mode:
        last_item = "\n\n---\n\n" + last_item + "\n\n---\n"
    else:
        last_item = "\n---\n\n" + last_item + "\n\n---\n"
    last_item = last_item.encode("utf-8")
    # print(last_item)

    # return

    write_success = False
    try:
        if append_mode:
            note_file = open(full_path, "ab")
        else:
            note_file = open(full_path, "wb")
        note_file.write(last_item)
        note_file.close()
        write_success = True
    except Exception as ex:
        print(ex)

    keyword = "generate"
    if append_mode:
        keyword = "update"
    if write_success:
        print(keyword + " note file %s" % full_path)
    else:
        print(keyword + " note file failed!")

main()
print("done!")
