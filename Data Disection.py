import statistics as stat
import csv

file  = open("vehicle_insurance_claims.csv", "r")
#print(file.readline())

lines = []
for line in file:
    appended = []
    for iter in line.split(","):
        appended.append(iter)
    lines.append(appended)

for i in range(len(lines[0])):
    print(i, end=" ")
    print(lines[0][i])

def getIndexOf(lister, obj):
    for i in range(len(lister)):
        if (lister[i]==obj):
            return i
    return -1

states = []
locations = []
parallel = []
for i in range(1, len(lines)):
    adderString = lines[i][22] + " " + lines[i][23]
    if adderString not in locations:
        locations.append(adderString)
        parallel.append(1)
    else:
        parallel[getIndexOf(locations, adderString)]+=1
    
sortedLocations = []
for i in range(len(locations)):
    print(locations[i], end = " ")
    print(parallel[i])
    sortedLocations.append(locations[i] + " " + str(parallel[i]))

sortedLocations = sorted(sortedLocations)
num = 0
for i in sortedLocations:
    print(num, end = " ")
    print(i)
    num+=1

rows = []
for i in sortedLocations:
    rows.append(i.split(" "))
print(rows)

fields = ["State", "City", "Number Of Occurences"]
filename = "UpdatingNecessary.csv"

with open(filename, 'w', newline="") as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 