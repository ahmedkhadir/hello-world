# csv2xml.py

# Fourth row of the csv file must be header!
#just added another comment to try github branch + open and merge pull request

import csv
import codecs

def csv2xml(csvFile, xmlFile):


    #csvData = open(csvFile, 'r+')
    csvData = csv.reader(codecs.open(csvFile, 'rU'))#, 'utf-16-le'
    xmlData = open(xmlFile, 'w')
    xmlData.write('<?xml version="1.0" encoding="UTF-8"?>' + "\n")

    xmlData.write('<jtol_data>' + "\n")
    #print (csvData)

    rowNum = 0
    for row in csvData:

        if rowNum == 0:
            #next(csvData)
            #next(csvData)
            #next(csvData)
            next(csvData)
            tags = next(csvData)
            next(csvData)
            #tags = row
            #print(row)
            print(tags)
            


            # replace spaces w/ underscores in tag names
            """
            for i in range(len(tags)):
                tags[i] = tags[i].replace(' ', '_')
                #print(tags[0])
            """
        else: 
            xmlData.write('<row>' + "\n")
            for i in range(len(tags)):
                xmlData.write('    ' + '<' + tags[i] + '>' \
                              + row[i] + '</' + tags[i] + '>' + "\n")
                #print(i, rowNum)
            xmlData.write('</row>' + "\n")
                
        rowNum +=1

    xmlData.write('</jtol_data>' + "\n")
    xmlData.close()


csv2xml(csvFile = "temp1.csv", xmlFile = "temp1.xml")
