import csv
import math

with open('aggregateReport.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    readerList = list(spamreader)
    url = readerList[1][0]
    resultsRow = readerList[-1]

    meanValue = resultsRow[2]
    x = abs(int(resultsRow[2]) - int(resultsRow[3]))
    stdDeviation = math.sqrt(x)

    print("URL: " + url + "  Mean: " + resultsRow[2] + "  Standard Deviation: " + str(stdDeviation))
