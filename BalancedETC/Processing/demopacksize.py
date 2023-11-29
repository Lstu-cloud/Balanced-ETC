import csv
result = []
linecount = 0
with open(r'E:\ProjectFP\ProjectFP\FlowPic-main\FlowPic_raw_csvs\test_pcaps\Skype.csv', "r", encoding='utf8', newline='') as f:
    # total = len(f.readlines())
    reader = csv.reader(f)

    for row in reader:
        linecount += 1
        time_counts = row[7]
        common_data = row[:7]
        line = []
        # timestamps = row[9 + int(time_counts):9 + 2*int(time_counts)]
        timestamps = row[9 + int(time_counts):34+ int(time_counts)]
        for index in range(len(timestamps) ):
            diff = float(timestamps[index])
            diff = float(diff)/1500
            diff = float(diff)*255
            diff = int(diff)
            line.append((diff))
        print(linecount, "line process over")
        result.append(line)
        pass

linecount = 0
with open(r'E:\ProjectFP\ProjectFP\FlowPic-main\FlowPic_raw_csvs\test_pcaps\1PS-Skype.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ')
    for item in result:
        spamwriter.writerow('{:5f},'.format(i) for i in item)

# for item in result:
# 	spamwriter.writerow(item)
#     # print(linecount,"line write over")