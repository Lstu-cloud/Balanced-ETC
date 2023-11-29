import csv
result = []
linecount = 0

import os

filepath = r'C:\Processing_classification\Processing_classification\Processing_classification\split_output'


def read(filepath,n):
    files = os.listdir(filepath)

    for el in files:
        fp = os.path.join(filepath, el)
        if os.path.isdir(fp):
            print("\t" * n, el)
            read(fp, 1 + 1)
        else:
            print("\t" * 1, el)

        with open(fp, "r", encoding='utf8', newline='') as f:
            # total = len(f.readlines())
            reader = csv.reader(f)
            linecount = 0

            for row in reader:
                linecount += 1
                line = []
                timestamps = row[0:100]
                for index in range(len(timestamps)):
                    diff = int(timestamps[index], 16)
                    line.append((diff))
                print(linecount, "line process over")
                result.append(line)
                pass

        linecount = 0
        with open(fp, 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=' ')
            for item in result:
                spamwriter.writerow('{:5f},'.format(i) for i in item)


read(filepath, 0)



