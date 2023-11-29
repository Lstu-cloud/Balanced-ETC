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

            file_path1 = fp
            # file_path2 = r'E:\ProjectFP\ProjectFP\FlowPic-main\TrafficParser\aaa516\1iscx_chat_raw.csv'
            file_path2 ='700Torrent' + el

            i = 1
            with open(file_path1) as f:
                csv_read = csv.reader(f)
                with open(file_path2, 'w', newline='') as f_w:
                    f_csv = csv.writer(f_w)
                    for content in csv_read:
                        # print(content)
                        f_csv.writerow(content)
                        i = i + 1
                        if i > 21:
                            break

read(filepath, 0)



