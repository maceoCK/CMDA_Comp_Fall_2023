import statistics as stat
import csv

file = open("City Crashes with updated populations and pop density and gov spending.csv","r")
outFile = "CleanedData.csv"
#Skip first line of headers
headers = next(file).split(',')

#Iterate through the rest of the file and write to csv
with open (outFile, "w", newline="") as csvfile:
    csvWrite = csv.writer(csvfile)
    csvWrite.writerow(headers)
    for row in file:
        line = row.split(',')
        if line[3].isnumeric():
            csvWrite.writerow(line)