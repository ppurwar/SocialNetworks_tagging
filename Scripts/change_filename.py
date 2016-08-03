import time
import os
import json
import glob
import re

for filename in glob.iglob('x*'):
    print "b fn: ",filename
    data_file = open(filename)   
    for time_val in data_file:
        #print "val : ",time_val
        y = 'time' in time_val
        #print "y :",y
        x = time_val.find("time")
        #print "x :",x
        #if(x!=-1):
        if(y):
            #print "str : ",time_val[1:10]
            tt = time_val.partition(':')[-1].rpartition(',')[0]
            ##print "tt str : ",tt
            time_new=time.ctime(float(tt))
            ##print "time new str : ",time_new
            words = re.split('\s+', time_new)
            ##print "words :",words
            file_str = words[2]+'_'+words[1]+'_'+words[4]+'_'+words[3]+'.json'
            ##print "filename :",file_str
            break



    ##print "got time so break \n"
    os.rename(filename, file_str)
    print "change the file from : ",filename," to new filename : ", file_str
