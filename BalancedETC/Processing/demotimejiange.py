import csv
result=[]
linecount=0
with open(r'E:\ProjectFP\ProjectFP\FlowPic-main\FlowPic_raw_csvs\test_pcaps\VOIP-buster.csv', "r",encoding='utf8',newline='') as f:
	# total = len(f.readlines())
	reader = csv.reader(f)
	
	for row in reader:
		linecount+=1
		time_counts=row[7]
		common_data=row[:7]
		line=[]
		timestamps=row[8:8+int(time_counts)]
		# timestamps=row[8:33]
		for index in range(len(timestamps)-1):
			diff=float(timestamps[index+1])-float(timestamps[index])
			diff=diff * 100
			line.append((diff))
		print(linecount,"line process over")
		result.append(line)
		pass

linecount=0
with open(r'E:\ProjectFP\ProjectFP\FlowPic-main\FlowPic_raw_csvs\test_pcaps\3PT-VOIP-buster.csv', 'w', newline='') as csvfile:
	spamwriter = csv.writer(csvfile, delimiter=' ')
	for item in result:
		spamwriter.writerow('{:5f},'.format(i) for i in item)



    # for item in result:
    # 	spamwriter.writerow(item)
	#     # print(linecount,"line write over")