#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy
from collections import OrderedDict

reload(sys)
sys.setdefaultencoding('utf-8')


def read_file(textfile):
    """
    Read *.txt file which is exported in KakaoTalk App.
    """
    with open(textfile,'r') as rf:
        for line in rf:
            if len(line) > 0:
                _read_line(line)


def _read_line(line):
    """
    Read each line and seperate date and comments.
    """
    splited = line.split(':')
    if len(splited) > 2:
        _read_word(splited[2].strip())


word_dic = dict()


def _read_word(line):
    """
    """
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


def print_dict(dic_source):
    """
    Print dict data looks like [word] : count
    """
    if len(dic_source) > 0:
        for key in dic_source:
            print "[%s] : %d" % (key, dic_source[key])


def sorted_dict(raw_dic):
    """
    Sort dict values.
    """
    sorted_dic = OrderedDict(sorted(raw_dic.items(), key=lambda x: x[1], reverse=True))

    return sorted_dic


def _save_to_txtfile(dic_data):
    """
    Save dict data to result.txt file.
    """
    with open('result.txt', 'w') as wf:
        for key in dic_data:
            line = str(unicode(key))+":"+str(dic_data[key])+"\n"
            wf.write(line)


if __name__ == "__main__":

    if len(sys.argv)  > 1:
        input_file = sys.argv[1]
        read_file(input_file)
        sorted_dic = sorted_dict(word_dic)
        print_dict(sorted_dic)
    else:
        sys.stderr.write("You should add input txt file!\n")
        sys.stderr.write("Looks like 'python katalklog.py sample.txt'\n")
        raise SystemExit(1)
