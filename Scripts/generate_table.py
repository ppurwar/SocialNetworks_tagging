############################################################
#Parse the json data into an excel file in below format
#Start Time     Tag A	Tag B   End Time 
#11:55:12       8023    8092    11:58:31 	 
############################################################

import json
import time
import re
import glob
import numpy as np
import csv

def convert_to_sec(time_format):
    #print "time:",time_format
    time_new=time.ctime(float(time_format))
    words = re.split('\s+', time_new)
    start_time = words[3]
    #print "hh:mm:ss time fmt:",start_time
    words = re.split(':', start_time)
    time_in_sec=(int(words[0])*3600)+(int(words[1])*60)+int(words[2])
    
    return time_in_sec

def convert_to_hh_mm_ss(time_format):
    #print "time:",time_format
    time_new=time.ctime(float(time_format))
    words = re.split('\s+', time_new)
    time_in_hh_mm_ss = words[3]
    #print "hh:mm:ss time fmt:",time_in_hh_mm_ss
    #words = re.split(':', start_time)
    #time_in_sec=(int(words[0])*3600)+(int(words[1])*60)+int(words[2])
    
    return time_in_hh_mm_ss


######################################################
# Variables to control the delete and merge time
#The minimal length of an interaction should be 10 seconds
consider_time=10

#The maximal time between 2 interactions should be < 30 seconds
#If less than 30 sec, merge them together
merge_time=30
######################################################

csvFile = open('Tags_Interation_table.csv', 'w')
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')

count=0
##Sheet to save Excel file
csvWriter.writerow(['Start Time','System start time','Tag A','Tag B','End Time','System end time'])

# Dynamic Arrays to store the interaction values from json file
arr_store_val = np.zeros((1,5))
arr_store_tmp = np.zeros((1,5))
entries_in_array=0
not_unique=0
list_of_interactions=[[]]
no_of_valid_interactions=0
for filename in glob.iglob('123*.json'):
    #print filename
    ##print "count",count
    data_file = open(filename).read()    
    data_json = json.loads(data_file)
      
    for key in data_json:
        if key.has_key("edge"):
            time_val=str(key['time'])
            #print "start time to populate:",time_val
            time_new=time.ctime(float(time_val))
            #print "time new str : ",time_new
            words = re.split('\s+', time_new)
            #print "words :",words
            time_final = words[3]+'_'+words[2]+'_'+words[1] 
            
            #not_unique=0
 
            for edge_key in key['edge']:
                #print "count",count
                not_unique=0
                #print "id:",key['id']
                ##print "time:",key['time']
                #print "tag:",edge_key['tag']
                #print "power:",edge_key['power']
                count=count+1
                
                sum_of_end_time_missing=sum(arr_store_val[:,3]) 
                #print "sum of end_time missing", sum_of_end_time_missing
                
                #if(sum_of_end_time_missing>0):
                for index in arr_store_val:
                    if(index[0]!=0):
                        #print "index", index[1]
                        #print "index", index[2]
                        #print "arr in for",arr_store_val
                        #print "tag to match", edge_key['tag'][0]
                        #print "tag to match", edge_key['tag'][1]
                        #print "entry no", index[4]
                        if(index[1]==edge_key['tag'][0] and index[2]==edge_key['tag'][1]):
                            not_unique=1
                            #print "match", edge_key['tag'][0]
                            #print "match", index[2]
                            #print "keep the array"
                            break
                        else:
                            not_unique=0
                            #print "unique ele"
                
                #print "not_unique",not_unique
                if(entries_in_array==0 or not_unique==0):
                    arr_store_val[entries_in_array][0]=key['time']
                    arr_store_val[entries_in_array][1]=edge_key['tag'][0]
                    arr_store_val[entries_in_array][2]=edge_key['tag'][1]
                    arr_store_val[entries_in_array][3]=1
                    arr_store_val[entries_in_array][4]=entries_in_array
                    #print "arr entry0:",arr_store_val[entries_in_array]
                    #if(entries_in_array>0):
                    entries_in_array=entries_in_array+1
                    #append 0s for next row
                    arr_store_val=np.append(arr_store_val,arr_store_tmp,axis=0)#arr_store_val[entries_in_array], axis=0)
                    #print "arr entry:",arr_store_val
                #    #print "tag:",edge_key['tag'][0]
                
                # have to delete the element
            #for index 
            index_to_delete=0 
            for index in arr_store_val:
                if(index[0]!=0):
                    #print "index tim",index[0]
                    #print "index tg1",index[1]
                    #print "index tg2",index[2]
                    #print "index_to_delete",index_to_delete
                    match_found=0
                    for edge_key in key['edge']:
                        #print "ele check to delete"
                        #print "edge tag0",edge_key['tag'][0]
                        #print "edge tag1",edge_key['tag'][1]
                        if(index[1]==edge_key['tag'][0] and index[2]==edge_key['tag'][1]):
                            match_found=1
                            #index_to_delete=index_to_delete+1
                            break
                        else:
                            match_found=0
                            #index_to_delete=index_to_delete+1
                            #index_to_delete=index[4]

                    #print "match_found:",match_found
                    if(index[0]!=0 and match_found == 0):
                        #delete the array
                        #print "edge to delet",index[1]
                        #print "edge to delet",index[2]
                        #print "ele not found so delete",index_to_delete
                        ##now add to list
                        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][0]))
                        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][1]))
                        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][2]))
                        list_of_interactions[no_of_valid_interactions].append(key['time'])
                        #print "end time to populate:",time_val
                        #list_of_interactions[no_of_valid_interactions].append(time_val)
                        #list_of_interactions[no_of_valid_interactions].append(arr_store_val[index_to_delete][4])
                        list_of_interactions.append([])
                        no_of_valid_interactions = no_of_valid_interactions + 1
                        #print "list:",list_of_interactions
                        #print "arr_store_val b :",arr_store_val
                        arr_store_val=np.delete(arr_store_val, index_to_delete, 0)
                        #print "arr_store_val a :",arr_store_val
                        entries_in_array=entries_in_array-1
                        index_to_delete=index_to_delete-1

                    index_to_delete=index_to_delete+1



        else:
            #No Key found, means all interactions before have ended
            for index in arr_store_val:
                #print "el index td",index[1]
                #print "el index td",index[2]
                index_to_delete=0 
                if(index[0]!=0):
                    list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][0]))
                    list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][1]))
                    list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][2]))
                    list_of_interactions[no_of_valid_interactions].append(key['time'])
                    list_of_interactions.append([])
                    no_of_valid_interactions = no_of_valid_interactions + 1
                    #print "ke list:",list_of_interactions
                    #print "ke arr_store_val b :",arr_store_val
                    arr_store_val=np.delete(arr_store_val, index_to_delete, 0)
                    #print "ke arr_store_val a :",arr_store_val
                    entries_in_array=entries_in_array-1
                    index_to_delete=index_to_delete+1


                #csvWriter.writerow([key['id'],time_final,edge_key['tag'],edge_key['power']])
                #worksheet.write(count, 0, key['id'])
                #worksheet.write(count, 1, time_final)
                #worksheet.write(count, 2, str(edge_key['tag']))
                #worksheet.write(count, 3, str(edge_key['power']))
            
            #check if end time doesn't have a value
            #if():

#print "count",count
#print "list:",list_of_interactions
#print "arr_store_val f b :",arr_store_val
#Last Interactions which started at the end of experiements & still haven't got over
for index in arr_store_val:
    #print "index td",index[1]
    #print "index td",index[2]

    index_to_delete=0 
    if(index[0]!=0):
        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][0]))
        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][1]))
        list_of_interactions[no_of_valid_interactions].append(int(arr_store_val[index_to_delete][2]))
        list_of_interactions[no_of_valid_interactions].append(key['time'])
        list_of_interactions.append([])
        no_of_valid_interactions = no_of_valid_interactions + 1
        #print "e list:",list_of_interactions
        #print "e arr_store_val b :",arr_store_val
        arr_store_val=np.delete(arr_store_val, index_to_delete, 0)
        #print "e arr_store_val a :",arr_store_val
        entries_in_array=entries_in_array-1
        index_to_delete=index_to_delete+1


#print "list:",list_of_interactions
#print "arr_store_val f a :",arr_store_val
del list_of_interactions[-1]
list_of_interactions = sorted(list_of_interactions)
## Save to an excel file
for list_index in list_of_interactions:
    #print "list_index:",list_index
    #start and end time of interaction
    time_val_start=str(list_index[0])
    start_time_hh_mm_ss = convert_to_hh_mm_ss(time_val_start)
    #print "start_time_hh_mm_ss",start_time_hh_mm_ss
    
    #end_time=
    time_val_end=str(list_index[3])
    end_time_hh_mm_ss = convert_to_hh_mm_ss(time_val_end)
    #print "end time :",end_time_hh_mm_ss
    
    #Write to Excel Field
    csvWriter.writerow([start_time_hh_mm_ss,time_val_start,list_index[1],list_index[2],end_time_hh_mm_ss,time_val_end])
                
##print "count",count
#workbook.close()
csvFile.close()

##print "introduce the consider and merge time"
counter=1
#list_of_interactions = sorted(list_of_interactions)
len_of_list=len(list_of_interactions)
#print "list len ",len_of_list


#######################################################
# Step 1
# To merge interactions with less than 30 seconds gap
#######################################################

#print "list_of_interactions before",list_of_interactions
index_in_search=0

for list_index in list_of_interactions:
    #print "list_index:",list_index
    #print "counter:",counter
    #print "index_in_search:",index_in_search
        
    time_val_end=str(list_index[3])
    #time_val_start=str(list_index[0])
    time_in_sec_to_search=convert_to_sec(time_val_end)
    tag_A_to_search=list_index[1]    
    tag_B_to_search=list_index[2]    
    #print "time_in_sec_to_search",time_in_sec_to_search
    #print "tag_A_to_search",tag_A_to_search
    #print "tag_B_to_search",tag_B_to_search
    
    index = counter
    while(index < len(list_of_interactions)):
    #for index in range(counter,len(list_of_interactions)):
        tag_A_val=list_of_interactions[index][1]
        tag_B_val=list_of_interactions[index][2]
        #print "tag_A_val",tag_A_val
        #print "tag_B_val",tag_B_val
        #print "index",index
        #print "len of list",len(list_of_interactions)
        current_time_val=list_of_interactions[index][0]
        #print "current_time_val",current_time_val
        #print "prev_time_val",time_in_sec_to_search
        current_time_in_sec=convert_to_sec(current_time_val)
        #print "current_time_in_sec",current_time_in_sec
        diff_in_sec=current_time_in_sec-time_in_sec_to_search
        #print "diff_in_sec :",diff_in_sec
        #print "list_of_interactions",list_of_interactions[index]
        
        if(diff_in_sec > merge_time):
            #print "break"
            break
        
        if(tag_A_val==tag_A_to_search and tag_B_val==tag_B_to_search):
            #print "same tag id found, merge"
            #print "list_of_interactions if b",list_of_interactions
            #print "counter",counter
            #list.pop to remove the interaction & merge with earlier one
            current_end_time_val=list_of_interactions[index][3]
            #print "current_end_time_val",current_end_time_val
            time_in_sec_to_search=convert_to_sec(current_end_time_val)
            list_of_interactions[index_in_search][3]=current_end_time_val
            pop_val=list_of_interactions.pop(index)
            #print "pop_val",pop_val
            #counter=counter-1
            #index_in_search=index_in_search-1
            #print "list_of_interactions if a",list_of_interactions
            #break
        index=index+1
        ##print "list_of_interactions",list_of_interactions[index]

    counter=counter+1
    index_in_search=index_in_search+1
        #Check for above index till 30seconds then break 
        #for list_index in list_of_interactions:
            #if() 

#print "list_of_interactions after",list_of_interactions

#######################################################
# Step 2
# To remove interactions with less than 10 seconds
#######################################################

index_to_delete=0
list_of_interactions_after_deletion=[[]]
for list_index in list_of_interactions:
    
    time_val_start=str(list_index[0])
    time_in_sec_to_start=convert_to_sec(time_val_start)
   
    time_val_end=str(list_index[3])
    time_in_sec_to_end=convert_to_sec(time_val_end)
    
    #print "list index",list_index
    #print "time_in_sec_to_start :",time_in_sec_to_start
    #print "time_in_sec_to_end :",time_in_sec_to_end

    diff_in_sec = time_in_sec_to_end-time_in_sec_to_start
    print "diff_in_sec :",diff_in_sec
    #if (diff_in_sec<consider_time):
        #print "need to erase the interaction"
        #pop_val=list_of_interactions.pop(index_to_delete)
        ##print "pop_val",pop_val
        #index_to_delete=index_to_delete-1
        #continue
    #else:
    if(diff_in_sec>consider_time):
        print "keep the interaction"
        list_of_interactions_after_deletion[index_to_delete]=list_index
        list_of_interactions_after_deletion.append([])
        index_to_delete=index_to_delete+1

    
    #print "index_to_delete",index_to_delete

del list_of_interactions_after_deletion[-1]
#print "list_of_interactions final",list_of_interactions
#print "list_of_interactions final",list_of_interactions_after_deletion


#######################################################
# Step 3
# To create ties which are missing  
#######################################################

list_of_interactions_with_ties=[[]]
counter=1
index_of_list_to_add=0

for list_index in list_of_interactions_after_deletion:
    #print "i list_index:",list_index
    #print "i counter:",counter
        
    time_val_end=str(list_index[3])
    time_val_start=str(list_index[0])
    time_in_sec_to_search_end=convert_to_sec(time_val_end)
    time_in_sec_to_search_start=convert_to_sec(time_val_start)
    
    tag_A_to_search=list_index[1]    
    tag_B_to_search=list_index[2]    
    
    ##original interaction
    list_of_interactions_with_ties[index_of_list_to_add]=list_index 
    list_of_interactions_with_ties[index_of_list_to_add].append('Observed')
    list_of_interactions_with_ties.append([]) 
    index_of_list_to_add=index_of_list_to_add+1

    #print "i time_in_sec_to_search",time_in_sec_to_search
    #print "i tag_A_to_search",tag_A_to_search
    #print "i tag_B_to_search",tag_B_to_search
    #print "i list_of_interactions_with_ties",list_of_interactions_with_ties
    
    index = counter
    while(index < len(list_of_interactions_after_deletion)):
    #for index in range(counter,len(list_of_interactions)):
        tag_A_val=list_of_interactions_after_deletion[index][1]
        tag_B_val=list_of_interactions_after_deletion[index][2]
        #print "f tag_A_val",tag_A_val
        #print "f tag_B_val",tag_B_val
        #print "f index",index
        #print "f len of list",len(list_of_interactions)
        current_time_val_start=list_of_interactions_after_deletion[index][0]
        current_time_val_start_in_sec=convert_to_sec(current_time_val_start)
        current_time_val_end=list_of_interactions_after_deletion[index][3]
        current_time_val_end_in_sec=convert_to_sec(current_time_val_end)
        #print "f current_time_val_start_in_sec",current_time_val_start_in_sec
        #print "f current_time_val_end_in_sec",current_time_val_end_in_sec
        
        #if ccurrent time is greater than end_time of search interaction we can break as no overlaps
        if(time_in_sec_to_search_start<=current_time_val_start_in_sec and current_time_val_start_in_sec<=time_in_sec_to_search_end):
            #match either of Tag A/B, create the 3rd tie between new Tag C with Tag A/B
            #if(tag_A_val==tag_A_to_search and tag_B_val==tag_B_to_search):
                #print "do nothing"
            if(tag_A_val==tag_A_to_search and tag_B_val!=tag_B_to_search):
                #print "create new tie b/w B and C"
                list_of_interactions_with_ties[index_of_list_to_add].append(current_time_val_start)
                list_of_interactions_with_ties[index_of_list_to_add].append(tag_B_to_search)
                list_of_interactions_with_ties[index_of_list_to_add].append(tag_B_val)
                if(time_in_sec_to_search_end>current_time_val_end_in_sec):
                    list_of_interactions_with_ties[index_of_list_to_add].append(current_time_val_end)
                else:
                    list_of_interactions_with_ties[index_of_list_to_add].append(int(time_val_end))

                list_of_interactions_with_ties[index_of_list_to_add].append('Created')
                list_of_interactions_with_ties.append([]) 
                index_of_list_to_add=index_of_list_to_add+1
                #print "list_of_interactions_with_ties",list_of_interactions_with_ties
                
            elif(tag_B_val==tag_B_to_search and tag_A_val!=tag_A_to_search):
                #print "create new tie b/w A and C"
                list_of_interactions_with_ties[index_of_list_to_add].append(current_time_val_start)
                list_of_interactions_with_ties[index_of_list_to_add].append(tag_A_to_search)
                list_of_interactions_with_ties[index_of_list_to_add].append(tag_A_val)
                if(time_in_sec_to_search_end>current_time_val_end_in_sec):
                    list_of_interactions_with_ties[index_of_list_to_add].append(current_time_val_end)
                else:
                    list_of_interactions_with_ties[index_of_list_to_add].append(int(time_val_end))
                
                list_of_interactions_with_ties[index_of_list_to_add].append('Created')
                list_of_interactions_with_ties.append([]) 
                index_of_list_to_add=index_of_list_to_add+1
                #print "list_of_interactions_with_ties",list_of_interactions_with_ties
        else:
            #print "break"
            break

        index=index+1
    counter=counter+1

#print "list_of_interactions_with_ties b",list_of_interactions_with_ties
del list_of_interactions_with_ties[-1]
#print "list_of_interactions_with_ties a",list_of_interactions_with_ties

#######################################################
# To write to csv file final list of interactions
#######################################################

csvFile = open('Final_Tags_Interation_table.csv', 'w')
csvWriter = csv.writer(csvFile, delimiter=',', lineterminator='\n')
csvWriter.writerow(['Start Time','Interaction system start time','Tag A','Tag B','End Time','Interaction system end time','Interaction observed/created'])

for list_index in list_of_interactions_with_ties:
    #print "list_index:",list_index
    #start and end time of interaction
    time_val_start=str(list_index[0])
    time_in_sec_start_time=convert_to_hh_mm_ss(time_val_start)
    #print "start time :",time_in_sec_start_time
   
    #end_time
    time_val_end=str(list_index[3])
    time_in_sec_end_time=convert_to_hh_mm_ss(time_val_end)
    #print "end time :",time_in_sec_end_time
    
    #Write to Excel Field
    #csvWriter.writerow([start_time,list_index[1],list_index[2],end_time])
    csvWriter.writerow([time_in_sec_start_time,time_val_start,list_index[1],list_index[2],time_in_sec_end_time,time_val_end,list_index[4]])
                
##print "count",count
#workbook.close()
csvFile.close()

