############################################################
#Parse the json data into an excel file in below format
#ID, actual time	    Dyad(Tags)	    Power
# 2	 11:55:12_15_Jul    8023, 8092 	 3
############################################################

import json
import time
import re
import glob
import csv

## Excel file name to save the data
csvFile = open('Tags_Interation_data.csv', 'w')
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
#csvWriter = csv.writer(csvFile, lineterminator='\n')
   

count=0
##Sheet to save Excel file
csvWriter.writerow(['ID','Time','Tags','Intensity'])

for filename in glob.iglob('*.json'):
    print filename
    print "count",count
    data_file = open(filename).read()    
    data_json = json.loads(data_file)
    
    for key in data_json:
        if key.has_key("edge"):
            time_val=str(key['time'])
            #print time_val
            time_new=time.ctime(float(time_val))
            #print "time new str : ",time_new
            words = re.split('\s+', time_new)
            #print "words :",words
            time_final = words[3]+'_'+words[2]+'_'+words[1] 
    
            for edge_key in key['edge']:
                #print "count",count
                #print "id:",key['id']
                #print "time:",key['time']
                #print "tag:",edge_key['tag']
                #print "power:",edge_key['power']
                count=count+1
                csvWriter.writerow([key['id'],time_final,edge_key['tag'],edge_key['power']])
    
print "count",count
csvFile.close()
