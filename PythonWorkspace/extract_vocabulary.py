#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import re
import random
import nltk

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")

def extract_vocabulary(sentences, **kargs):
    '''
    Extract word by NLTK.
    Default way.
    '''
    vocabulary = set()
    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        for word in words:
            if len(word) <= 2:
                continue
            vocabulary.add(word.lower())
    return vocabulary

def extract_vocabulary_way_1(sentences, **kargs):
    '''
    Extract word by spaces.
    '''
    vocabulary = set()
    for sentence in sentences:
        words = sentence.split(" ")
        words = [word.lower() for word in words if len(word) > 2]
        vocabulary.update(words)
    return vocabulary

def extract_vocabulary_way_2(sentences, **kargs):
    '''
    Extract word.
    '''
    vocabulary = set()
    for sentence in sentences:
        mat = re.search("^##\s*([^#]+)$", sentence)
        if not mat:
            continue
        word = mat.group(1)
        vocabulary.add(word.strip())
    return vocabulary

def extract_vocabulary_way_3(sentences, **kargs):
    '''
    Extract word and explanation.
    '''
    vocabulary = []
    for sentence in sentences:
        mat = re.search(r"(^##\s*(?P<word>[^#]+)$)|(^([-*])*\s*\*\*Explanation:\*\*\s*(?P<explanation>.+)$)", sentence)
        if not mat:
            continue
        word = mat.group("word")
        explanation = mat.group("explanation")
        if word:
            vocabulary.append(word.capitalize().strip())
        if explanation:
            vocabulary.append(explanation.strip())

    # Word. Explanation.
    new_vocabulary = []
    index = 0
    current_line = ""
    for line in vocabulary:
        if index % 2 == 0:
            current_line = line + ". "
        else:
            current_line += line
            new_vocabulary.append(current_line)
            current_line = ""
        index += 1

    return new_vocabulary

def extract_vocabulary_way_4(sentences, **kargs):
    '''
    Extract word, then repeat.
    '''
    vocabulary = []
    for sentence in sentences:
        mat = re.search(r"(^##\s*(?P<word>[^#]+)$)|(^([-*])*\s*\*\*Explanation:\*\*\s*(?P<explanation>.+)$)", sentence)
        if not mat:
            continue
        word = mat.group("word")
        explanation = mat.group("explanation")
        if word:
            vocabulary.append(word.capitalize().strip())
        if explanation:
            vocabulary.append(explanation.strip())

    # Word. Word. Word.
    new_vocabulary = []
    index = 0
    current_line = ""
    for line in vocabulary:
        if index % 2 == 0:
            # current_line = line + ". "
            current_line = line
            current_line *= kargs.get("repeat_count", 2)
            new_vocabulary.append(current_line)
        index += 1

    return new_vocabulary

def extract_vocabulary_way_5(sentences, **kargs):
    '''
    TODO(zz) Extract explanation.
    '''
    vocabulary = []
    for sentence in sentences:
        mat = re.search(r"(^##\s*(?P<word>[^#]+)$)|(^([-*])*\s*\*\*Explanation:\*\*\s*(?P<explanation>.+)$)", sentence)
        if not mat:
            continue
        word = mat.group("word")
        explanation = mat.group("explanation")
        if word:
            vocabulary.append(word.capitalize().strip())
        if explanation:
            vocabulary.append(explanation.strip())

    # Word. Word. Word.
    new_vocabulary = []
    index = 0
    current_line = ""
    for line in vocabulary:
        if index % 2 == 0:
            # current_line = line + ". "
            current_line = line
            current_line *= kargs.get("repeat_count", 2)
            new_vocabulary.append(current_line)
        index += 1

    return new_vocabulary

def extract_vocabulary_way_6(sentences, **kargs):
    '''
    TODO(zz) Extract samples.
    '''
    vocabulary = []
    for sentence in sentences:
        mat = re.search(r"(^##\s*(?P<word>[^#]+)$)|(^([-*])*\s*\*\*Explanation:\*\*\s*(?P<explanation>.+)$)", sentence)
        if not mat:
            continue
        word = mat.group("word")
        explanation = mat.group("explanation")
        if word:
            vocabulary.append(word.capitalize().strip())
        if explanation:
            vocabulary.append(explanation.strip())

    # Word. Word. Word.
    new_vocabulary = []
    index = 0
    current_line = ""
    for line in vocabulary:
        if index % 2 == 0:
            # current_line = line + ". "
            current_line = line
            current_line *= kargs.get("repeat_count", 2)
            new_vocabulary.append(current_line)
        index += 1

    return new_vocabulary

def test_extract_vocabulary():
     # nltk.download('punkt')
    text = "Dr. Smith went to the hospital. He felt sick. What happened? Wow! This is an example. e.g. a test. This is the last sentence."
    sentences = nltk.sent_tokenize(text)
    vocabulary = extract_vocabulary(sentences)
    print(vocabulary)

'''
Extract vocabulary from a list of sentences.
'''
extract_vocabulary_way_list = [
    extract_vocabulary,
    extract_vocabulary_way_1,
    extract_vocabulary_way_2,
    extract_vocabulary_way_3,
    extract_vocabulary_way_4,
]

def extract_vocabulary_from_article(article_path, read_lines=False, way_index=0, **kargs):
    '''
    Extract vocabulary from a list of sentences.

    @return set or list.
    '''

    if read_lines:
        with open(article_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        sentences = lines
    else:
        with open(article_path, 'r', encoding='utf-8') as f:
            text = f.read()
        sentences = nltk.sent_tokenize(text)

    if way_index < 0 or way_index >= len(extract_vocabulary_way_list):
        return set()
    
    way = extract_vocabulary_way_list[way_index]
    vocabulary = way(sentences, **kargs.get("config", {}))
    return vocabulary

article_config_list = [
    {
        "index": 0,
        "article_path": os.path.join(ARTICLE_DIR, "Vocabulary-Meaning.md"), 
        "read_lines": True, 
        "way_index": 2,
        "shuffle": True,
        "vocabulary_as_set": True,
        "output_postfix": "vocabulary",
    },
    {
        "index": 1,
        "article_path": os.path.join(ARTICLE_DIR, "Vocabulary-Read.md"), 
        "read_lines": True, 
        "way_index": 2,
        "shuffle": True,
        "vocabulary_as_set": True,
        "output_postfix": "vocabulary",
    },
    {
        "index": 2,
        "article_path": os.path.join(ARTICLE_DIR, "Vocabulary-Spell.md"), 
        "read_lines": True, 
        "way_index": 2,
        "shuffle": True,
        "vocabulary_as_set": True,
        "output_postfix": "vocabulary",
    },
    {
        "index": 3,
        "article_path": os.path.join(ARTICLE_DIR, "Vocabulary-Phrase.md"), 
        "read_lines": True, 
        "way_index": 2,
        "shuffle": True,
        "vocabulary_as_set": True,
        "output_postfix": "vocabulary",
    },
    {
        "index": 4,
        "article_path": os.path.join("F:\\Obsidian\\Notes\\DefaultNotes\\世界\\澳新\\IELTS", "Vocabulary-Meaning.md"), 
        "read_lines": True, 
        "way_index": 3,
        "shuffle": False,
        "vocabulary_as_set": False,
        "output_postfix": "vocabulary",
    },
    {
        "index": 5,
        "article_path": os.path.join("F:\\Obsidian\\Notes\\DefaultNotes\\世界\\澳新\\IELTS", "Vocabulary-Meaning.md"), 
        "read_lines": True, 
        "way_index": 4,
        "shuffle": False,
        "vocabulary_as_set": False,
        "output_postfix": "reading",

        "repeat_count": 1,
    },
]
current_article_index = 5
current_article_config = article_config_list[current_article_index]

def main():
    random.seed()

    # test_extract_vocabulary()

    outputlines = []

    if current_article_config["vocabulary_as_set"]:
        vocabulary = set()

        # Batched:
        if False:
            for it_article_config in article_config_list:
                iter_vocabulary = extract_vocabulary_from_article(**it_article_config)
                vocabulary.update(iter_vocabulary)

            article_base_name = "all_in_one_vocabulary"
        else:
            vocabulary = extract_vocabulary_from_article(
                current_article_config["article_path"], 
                current_article_config["read_lines"], 
                current_article_config["way_index"])
            article_base_name = os.path.basename(current_article_config["article_path"]).split(".")[0]

        vocabulary = list(vocabulary)
        if current_article_config["shuffle"]:
            random.shuffle(vocabulary)

        # outputlines.append("Test will start in 3 seconds, countdown, 3, 2, 1, Go!")
        outputlines.extend(vocabulary)
        # outputlines.append("Test complete! Please check your answer and improve yourself, see you next time!")
    else:
        article_base_name = os.path.basename(current_article_config["article_path"]).split(".")[0]
        vocabulary = extract_vocabulary_from_article(
            current_article_config["article_path"], 
            current_article_config["read_lines"], 
            current_article_config["way_index"],
            **{ "config": current_article_config}
        )
        outputlines.extend(vocabulary)

    output_script_path = os.path.join(ARTICLE_DIR, f"{article_base_name} - {current_article_config['output_postfix']}.txt")
    outputlines = [f"{line}\n" for line in outputlines]
    with open(output_script_path, 'w', encoding='utf-8') as f:
        f.writelines(outputlines)

if __name__ == "__main__":
    main()
    print("done!")
