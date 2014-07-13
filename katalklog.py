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
    result = dict()

    with open(textfile,'r') as rf:
        for line in rf:
            if len(line) > 0:
                each_line = read_line(line)
                if each_line is not None:
                  split_line = each_line.split(' ')
                  for inner_line in split_line:
                    word = inner_line.strip()
                    if len(word) > 0:
                      encoded = unicode(word)
                      if encoded in result:
                          result[encoded] = result[encoded] + 1
                      else:
                          result[encoded] = 1
    return result


def read_data(data):
    result = dict()
    for line in data:
        if len(line) > 0:
            each_line = read_line(line)
            if each_line is not None:
              split_line = each_line.split(' ')
              for inner_line in split_line:
                word = inner_line.strip()
                if len(word) > 0:
                  encoded = unicode(word)
                  if encoded in result:
                      result[encoded] = result[encoded] + 1
                  else:
                      result[encoded] = 1
    return result

def read_line(line):
    """
    Read each line and seperate date and comments.
    """
    splited = line.split(':')
    if len(splited) > 2:
      return splited[2].strip()
    else:
      return None


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


def print_dict(dic_source):
    """
    Print dict data looks like [word] : count
    """
    if len(dic_source) > 0:
        for key in dic_source:
            print "[%s] : %d" % (key, dic_source[key])


if __name__ == "__main__":

    if len(sys.argv)  > 1:
        input_file = sys.argv[1]
        result = read_file(input_file)
        sorted_dic = sorted_dict(result)
        print_dict(sorted_dic)
    else:
        sys.stderr.write("You should add input txt file!\n")
        sys.stderr.write("Looks like 'python katalklog.py sample.txt'\n")
        raise SystemExit(1)
