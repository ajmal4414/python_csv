import csv

with open ('bus.csv') as file:
    reader=csv.reader(file)
    count=0
    for lines in reader:
        print(lines)
        if count>5:
            break
        count+=1
