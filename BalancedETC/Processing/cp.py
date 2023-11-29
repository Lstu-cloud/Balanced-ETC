import csv
result = []
linecount = 0

import os

from PIL import Image
import numpy as np
import re
import os

import pandas as pd

filepath = r'C:\Processing_classification\Processing_classification\Processing_classification\88PSPT'


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
            file_path2 ='868686' + el

            path = fp
            print(path)
            data_read = pd.read_csv(path)
            print(data_read.shape)
            list = data_read.values.tolist()
            # print(list[1])
            # print(list[1][1])
            # print(type(list[1][1]))
            counter1 = 1
            for i in range(len(data_read)):
                list = data_read.values.tolist()
                array1 = np.array(list[i])
                print(array1.shape)

                data = np.matrix(array1)
                data = np.reshape(data, (5, 5))

                im = Image.fromarray(np.uint8(data)).convert("L")
                # im.save(r'D:\ProjectFP\FlowPic-main\TrafficParser\out\outfile16.png')
                figure_save_path = '0'+el
                counter1 = str(counter1)
                if not os.path.exists(figure_save_path):
                    os.makedirs(figure_save_path)
                im.save(os.path.join(figure_save_path, counter1 + ".png"))
                counter1 = int(counter1)
                counter1 += 1





read(filepath, 0)
