import csv
from sys import argv  # command-line arguments
database = open(argv[1], 'r')  # open csv file
reader = csv.reader(database)  # read csv file
s = open(argv[2], 'r')  # open text file
se = s.read()  # read text file
seq = str(se)
strands = []  # to store DNA strands
dic = {}  # for the sequence and count for each STR
count = 0
for row in reader:
    strands = row  # copy STRs into strands list
    strands.pop(0)  # remove name
    break
for a in strands:
    for b in range(len(seq)):
        count = 0  # number of consecutive repetitions for each STR
        STR = seq[b:b + len(a)]
        if STR == a:  # check condition
            if not STR in dic.keys():
                count += 1  # increment count
                b += len(a)
                while STR == seq[b:b+len(a)]:  # compare adjacent strands
                    count += 1
                    b += len(a)
                dic[a] = count
            else:  # if strand is already in the dictionary
                count += 1
                b += len(a)
                while STR == seq[b:b+len(a)]:
                    count += 1
                    b += len(a)
                if count > dic[STR]:
                    dic[a] = count  # replace the current count by the longer one
                else:
                    continue
rec = []  # to store random people's dna
c = 0  # counter to check if all dna strands count matches the sequence given
for row in reader:
    rec = row
    j = 1
    c = 0
    for a in dic.keys():
        if dic[a] == int(rec[j]):  # if same number then success
            c += 1
        j += 1
    if c == len(rec) - 1:
        print(row[0])  # print the candidate's name if counter is 8 in case of large.csv
        break
if c < len(rec) - 1:
    print("No match")  # no match if its less
database.close()
s.close()
# close both files