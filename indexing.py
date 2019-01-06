import csv

data = {}
with open("violations.csv","r") as file_to_read:
	csv_to_read = csv.reader(file_to_read)
	for row in csv_to_read:
		if row[0] not in data:
			data[row[0]] = [row[1], row[3], row[7], 0]
		data[row[0]][3] += float(row[9]) ** (10.0/9.0)

print str(data)

with open("drvi.csv","w") as file_to_write:
	csv_to_write = csv.writer(file_to_write)
	for key in data:
		csv_to_write.writerow([key, data[key][0], data[key][1], data[key][2], data[key][3]])


#4872