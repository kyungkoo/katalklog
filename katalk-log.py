#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import copy
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')

word_dic = dict()

def read_file(textfile):
    with open(textfile,'r') as rf:
        for line in rf:
            if len(line) > 0:
                read_line(line)


def read_line(line):
    splited = line.split(':')
    if len(splited) > 2:
        read_word(splited[2].strip())


def read_word(line):

    splited = line.split(' ')
    for word in splited:
        if len(word) > 0:
            new_word = word.strip()
            if len(new_word) > 0:
                new_word = unicode(new_word)
                if new_word in word_dic:
                    word_dic[new_word] = word_dic[new_word] + 1
                else:
                    word_dic[new_word] = 1


def print_count():
    if len(word_dic) > 0:
        for key in word_dic:
            print "[%s] : [%d]" % (key, word_dic[key])

def sorted_dict():
    sorted_dic = OrderedDict(sorted(word_dic.items(), key=lambda x: x[1], reverse=True))

    with open('result.txt', 'w') as wf:
        for key in sorted_dic:
            line = str(unicode(key))+":"+str(sorted_dic[key])+"\n"
            wf.write(line)

if __name__ == "__main__":
    read_file('talk.txt')
    # print_count()
    sorted_dict()
