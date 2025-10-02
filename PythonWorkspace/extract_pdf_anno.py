import fitz  # PyMuPDF
import pyperclip
import sys
import os
import re
import inspect

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")
NOTES_DIR = "F:\\Obsidian\\Notes\\DefaultNotes\\World\\Australia-NewZealand\\IELTS\\Articles"
PDF_DIR = "F:\\Obsidian\\Notes\\DefaultNotes\\_Library\\_PDF"

'''
Bug250812:
    Output:
        en progress in yo
        comprehension
        t the level
        seminars
        d talk about l
        educational
    # The highlight area may larger than the text line, so it could covers more than one line, then we get this bug.
'''

def main():
    source_file_path = ""

    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.lexists(file_path):
            source_file_path = os.path.join(ARTICLE_DIR, file_path)
        if not os.path.lexists(source_file_path):
            source_file_path = os.path.join(NOTES_DIR, file_path)
        if not os.path.lexists(source_file_path):
            source_file_path = os.path.join(PDF_DIR, file_path)

    if not os.path.lexists(source_file_path):
        print(f"File {source_file_path} is not exist!")
        return
    
    print(f"extract words from {source_file_path}")

    doc = fitz.open(source_file_path)
    highlights = []

    for page in doc:
        for annot in page.annots():
            if annot.type[0] == 8:  # Highlight
                text = page.get_textbox(annot.rect) or annot.info["content"]
                mat = re.search(r"([\w\s]+)", text)
                word = ""
                if mat:
                    word = mat.group(1).strip()
                if len(word) > 0 and word not in highlights:
                    highlights.append(word)

    word_list_str = "\n".join(highlights)
    prompt = "Please make a vocabulary for the following word list:\n" + word_list_str
    print(prompt)
    pyperclip.copy(prompt)

if __name__ == "__main__":
    main()
    print("done!")
