import urllib.request
import os.path
# Imports libraries needed to do requests and things

if not(os.path.isfile('awslog.log')):  
    print('File not found. Downloading.')
    url = 'https://s3.amazonaws.com/tcmg476/http_access_log'
    urllib.request.urlretrieve(url, 'awslog.log')
    print('File downloaded. Resuming.')
    # checks for file, downloads if not there
    
f = open("awslog.log", "r")
#opens the log file, now named f

#text = f.read()
#reads from file into variable named text

#textList = text.split("\n")
#splits text by line

#textList = text.readlines()
#maybe alternative read lines?

countLine = 0
countMonthLine = 0
startMonthCount = False
#sets up variables for (in order) total line count, total line count of the last 6 months, the trigger for the start of counting the last six months

for line in f: #for every line in the file
    countLine+=1 #starts counting lines
    
    if '11/Apr/1995:00:00:16' in line: #starts the count at six months prior to the end of the file
        startMonthCount = True
        
    if startMonthCount == True:
        countMonthLine+=1 #counts the last six months
        
print("Number of requests/lines from the last 6 months of the log file:", countMonthLine)
print("Total Number of requests/lines in the log file:", countLine)
    
    
    
    
