import os
import csv
import zipfile
import sys

def extract_file(folder, name):
    for dirname, dirnames, filenames in os.walk(folder):
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
        for filename in filenames:
            if(filename.endswith(name)):
                zip_file = zipfile.ZipFile(os.path.join(dirname, filename))
                zip_file.extractall(os.path.join(dirname))

extract_file("C:/Users/abamboi/PycharmProjects/codewars/Client_script", ".zip")


def create_csv (location, csvext, columns):
    fd = open('summary1.csv', 'w')
    fieldnames = ['report', 'pos', 'neg', 'tot']
    writer = csv.DictWriter(fd, fieldnames)
    writer.writeheader()
    for dirname, dirnames, filenames in os.walk(location):
        for subdirname in dirnames:
            print(os.path.join(dirname, subdirname))
        for filename in filenames:
            if(os.path.join(dirname, filename).endswith(csvext)):
                pos = 0
                neg = 0
                tot = 0
                fd1 = open(os.path.join(dirname, filename), 'r')
                spamreader = csv.reader(fd1)
                key_names = csv.DictReader(fd1).fieldnames
                included_cols = columns
                for row in spamreader:
                    content = list(row[i] for i in included_cols)
                    pos_values = content[0]
                    neg_values = content[1]
                    tot_values = content[2]
                    print(pos_values, neg_values, tot_values)
                    for c in pos_values:
                        pos = pos + int(c)
                    for c in neg_values:
                        neg = neg + int(c)
                    for c in tot_values:
                        tot = tot + int(c)
                writer.writerow({'report':filename, 'pos':pos, 'neg':neg, 'tot':tot})
                print (pos, neg, tot)


create_csv("C:/Users/abamboi/PycharmProjects/codewars/Client_script", ".csv", [3, 4, -1])