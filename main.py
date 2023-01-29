import csv
#opening csv file
#with open('bus.csv', mode='r') as file:
#    reader=csv.reader(file)
#   for lines in reader:
#        print(lines)

#writing file

fields=['name','age','branch','place']

rows=[['joy',22,'cse','kannur'],
      ['tony',23,'mec','kochi'],
      ['roy',24,'civil','kottayam'],
      ['john',24,'civil','tvpm']]
filename="writingfile.csv"

with open('writing file.csv',mode='w') as file:
    writer=csv.writer(file)
    writer.writerow(fields)
    writer.writerows(rows)
