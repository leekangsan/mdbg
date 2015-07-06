__author__ = 'm.cherkasov'

import sys

try:
    file_name = sys.argv[1]
    print("filename: ", file_name)
    f = open(file_name)
    fw = open('chinese_dictionary.sql', 'w')
    i = 0
    for line in f:
        if line[0] != '#':
            str1 = line.split(" ")
            # print(str1[0], " ", str1[1], " ", line.partition('[')[-1].partition(']')[0])
            sql = "INSERT INTO study_platform.chinese_dictionary (traditional, simplified, pinyin) VALUES (" \
                  + "'" + str1[0] + "'," + "'" + str1[1] + "'," \
                  + "'" + line.partition('[')[-1].partition(']')[0] + "');"
            fw.write(sql + '\n')
            i += 1

    print("Lines: " + i)

except IndexError:
    print("usage: ", sys.argv[0], " <filename>")
except FileNotFoundError:
    print("File with name: ", file_name, " not found!")
