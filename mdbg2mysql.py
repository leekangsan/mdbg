__author__ = 'm.cherkasov'

import sys
import re
from bs4 import BeautifulSoup

def chinese_dictionary(input_file):
    f = open(input_file)
    fw = open('chinese_dictionary.sql', 'w')
    i = 0
    for line in f:
        if line[0] != '#':
            str1 = line.split(" ")
            pinyin = line.partition('[')[-1].partition(']')[0]
            pinyin_search = ''.join([i for i in pinyin.replace(' ', '') if not i.isdigit()])
            # print(str1[0], " ", str1[1], " ", line.partition('[')[-1].partition(']')[0])

            sql = "INSERT INTO study_platform.chinese_dictionary (traditional, simplified, pinyin, pinyin_search) VALUES (" \
                  + "'" + str1[0] + "'," + "'" + str1[1] + "'," \
                  + "'" + pinyin + "'," + "'" + pinyin_search + "');"

            fw.write(sql + '\n')
            i += 1

    print("Lines: ", i)


def extract_from_tag(tag, line):
    opener = "<" + tag + ">"
    closer = "</" + tag + ">"
    try:
        i = line.index(opener)
        start = i + len(opener)
        j = line.index(closer, start)
        return line[start:j]
    except ValueError:
        return None


def chinese_html(input_file):
    f = open(input_file, newline='', encoding='utf8')
    # fw = open('chinese_dictionary.sql', 'w')
    i = 0

    for line in f:
        tr = extract_from_tag("tr", line)
        if tr is not None:
            print(tr)
            i += 1

    print("Lines: ", i)


try:
    file_name = sys.argv[2]
    mode = sys.argv[1]
    print("filename: ", file_name)
    if mode == "html":
        f = open(file_name, newline='', encoding='utf8')
        soup = BeautifulSoup(f, 'html.parser')
        print(soup.find_all('tr'))
        # chinese_html(file_name)
    if mode == "dict":
        chinese_dictionary(file_name)

except IndexError:
    print("usage: ", sys.argv[0], " dict|html <filename>")
except FileNotFoundError:
    print("File with name: ", file_name, " not found!")
