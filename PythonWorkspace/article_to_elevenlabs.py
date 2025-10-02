#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
import re
import nltk

CUR_DIR = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
ARTICLE_DIR = os.path.join(CUR_DIR, "Articles")
SCRIPT_DIR = os.path.join(CUR_DIR, "Scripts")

def init_environment():
    # You might need to download the punkt tokenizer the first time:
    if not os.path.lexists(r"C:\Users\zhao_\AppData\Roaming\nltk_data"):
        nltk.download('punkt')

def test_nltk():
    text = "Dr. Smith went to the hospital. He felt sick. What happened? Wow! This is an example. e.g. a test. This is the last sentence."
    sentences = nltk.sent_tokenize(text)
    for s in sentences:
        print(s)

def article_to_sentence_list(file_path, read_lines=False):
    if read_lines:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        return lines
    else:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        return nltk.sent_tokenize(text)

def save_out_sentence_list(sentences, file_name):
    output_path = os.path.join(SCRIPT_DIR, file_name)
    with open(output_path, 'w', encoding='utf-8') as f:
        for s in sentences:
            f.write(s + "\n")

def count_words(sentence):
    words = nltk.word_tokenize(sentence)
    return len(words)

def clean_up_way(sentence):
    return sentence

def clean_up_way_1(sentence):
    sentence = sentence.strip()

    result = {
        "pos": -1,
        "result": sentence,
        "drop": False,
    }

    if len(sentence) <= 0:
        result["drop"] = True
        return False, result
    
    pos = sentence.find(": ")
    if pos <= 0:
        result["drop"] = True
        return False, result
    
    result["pos"] = pos + 2
    result["result"] = sentence[pos + 2:]
    return True, result

def clean_up_way_2(sentence):
    sentence = sentence.strip()

    result = {
        "pos": -1,
        "result": sentence,
        "drop": False,
    }

    result["result"] = sentence.rstrip()

    return True, result

clean_up_way_list = [
    clean_up_way, 
    clean_up_way_1, 
    clean_up_way_2
]

def clean_up_sentence_list(sentences, clean_up_ways=[]):
    # Cleanup
    new_sentences = []
    for sentence in sentences:
        new_sentence = sentence
        if len(clean_up_ways) > 0:
            for way_index in clean_up_ways:
                if way_index < 0 or way_index > len(clean_up_way_list):
                    break
                way = clean_up_way_list[way_index]
                ret, info = way(new_sentence)
                if ret:
                    new_sentence = info["result"]
                elif info["drop"]:
                    new_sentence = ""
                    break
                else:
                    break
        if len(new_sentence) > 0:
            new_sentences.append(new_sentence)

    return new_sentences

def reformat(sentences, format_type=0, repeat_count=1):
    new_sentences = []

    if format_type == 1:
        for sentence in sentences:
            new_sentence = sentence + ". "
            new_sentence *= repeat_count
            new_sentences.append(new_sentence)
        return new_sentences
    else:
        return sentences

article_info_list = [
    {
        "index": 0,
        "article_file_path": os.path.join(ARTICLE_DIR, "科幻大片《电幻国度》神还原各种机器人（下）.txt"),
        "read_line": False,
        "clean_up_way_list": [],
        "reformat_type": 0,

        "add_break_time": True,
        "add_speaker_and_end_break_time": True,
    },
    {
        "index": 1,
        "article_file_path": os.path.join(ARTICLE_DIR, "IELTS-Vocabulary-0.txt"),
        "read_line": True,
        "clean_up_way_list": [0],
        "reformat_type": 1,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,
    },
    {
        "index": 2,
        "article_file_path": os.path.join(ARTICLE_DIR, "all_in_one_vocabulary - word+explanation.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 0,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,
    },
    {
        "index": 3,
        "article_file_path": os.path.join(ARTICLE_DIR, "all_in_one_vocabulary - reading.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 1,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,

        # "output_basename_postfix": " - Reading",
    },
    {
        "index": 4,
        "article_file_path": os.path.join(ARTICLE_DIR, "Vocabulary-250629.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 0,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,

        # "output_basename_postfix": " - Reading",
    },
    {
        "index": 5,
        "article_file_path": os.path.join(ARTICLE_DIR, "Reading-250629.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 1,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,

        # "output_basename_postfix": " - Reading",
    },
    {
        "index": 6,
        "article_file_path": os.path.join(ARTICLE_DIR, "Vocabulary-Meaning - reading.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 1,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,

        # "output_basename_postfix": " - Reading",
        "repeat_count": 3,
    },
    {
        "index": 7,
        "article_file_path": os.path.join(ARTICLE_DIR, "Vocabulary-Meaning - vocabulary.txt"),
        "read_line": True,
        "clean_up_way_list": [2],
        "reformat_type": 0,

        "add_break_time": False,
        "add_speaker_and_end_break_time": True,

        # "output_basename_postfix": " - Reading",
    },
]
current_article_index = 7

def main():
    # test_nltk()

    current_article = article_info_list[current_article_index]

    article_path = current_article["article_file_path"]
    _, output_basename = os.path.split(article_path)
    output_basename, _ = os.path.splitext(output_basename)
    if "output_basename_postfix" in current_article:
        output_basename += current_article["output_basename_postfix"]

    sentences = article_to_sentence_list(article_path, current_article["read_line"])
    sentences = clean_up_sentence_list(sentences, current_article["clean_up_way_list"])
    sentences = reformat(sentences, current_article["reformat_type"], current_article.get("repeat_count", 1))

    output_sentences_pass0 = []
    if current_article["add_break_time"]:
        for sentence in sentences:
            words = sentence.split(" ")
            new_words = []
            for i, word in enumerate(words):
                new_words.append(word)
                if (i + 1) % 5 == 0:
                    new_words.append("<break time=\"3s\" />")
            sentence = " ".join(new_words)

            for i in range(2):
                output_sentences_pass0.append(sentence)
            # count = count_words(sentence)
            # if (count > 8):
            #     for _ in range(3):
            #         output_sentences_pass0.append(sentence)
            # elif (count > 15):
            #     for _ in range(4):
            #         output_sentences_pass0.append(sentence)
            # elif (count > 20):
            #     for _ in range(5):
            #         output_sentences_pass0.append(sentence)
            # else:
            #     output_sentences_pass0.append(sentence)
    else:
        output_sentences_pass0 = sentences

    output_sentences_pass1 = []
    if current_article["add_speaker_and_end_break_time"]:
        index = 0
        pause_time = "3"
        for sentence in output_sentences_pass0:
            index += 1
            if index % 2 == 1:
                speaker_name = "Aria"
            else:
                # TODO(zz) Bill
                speaker_name = "Aria"
            speaker_name = speaker_name + ": "
            output_sentences_pass1.append(sentence + f" <break time=\"{pause_time}s\" />")
    else:
        output_sentences_pass1 = output_sentences_pass0

    output_sentences_pass1.insert(0, "Test will start in 3 seconds, countdown, 3, 2, 1, Go!")
    output_sentences_pass1.append("Test complete! Please check your answer and improve yourself, see you next time!")
    save_out_sentence_list(output_sentences_pass1, f"{output_basename} - script.txt")

if __name__ == "__main__":
    init_environment()
    main()
    print("done!")
