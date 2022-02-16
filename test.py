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

text = f.read()
#reads from file into variable named text

textList = text.split("\n")
#splits text by line
