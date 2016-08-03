Readme to run the scripts

I) File : change_filename.py - To change the filenames from xaa* to meaning full names with start time stamp
    1.copy/download the python script to any directory where data is present
    2.execute below command
        python change_filename.py

II) File : generate_data.py
      run command : python generate_data.py
      Excecution of this command generates the "Tags_Interation_data.csv" csv file where all interactions for every second are captured with Intensity 
      
III) File : generate_table.py
      run command : python generate_table.py
      Excecution of this command generates 2 files.
      1. the "Tags_Interation_table.csv" file where the RAW data is collected with start and end time of all interactions without the below 3 step processing.
      
      2. the "Final_Tags_Interation_table.csv" file where all interactions are captured after performing below 3 steps:
        i)# To merge interactions with less than 30 seconds gap
            Variable to control - merge_time=30
        ii)# To remove interactions with less than 10 seconds
            Variable to control - consider_time=10
        iii) # To create ties which are missing  
            Example, if A interacts with B and B interacts with C, but A does not interact with C, then create a tie between A and C & mention a label as 'Created'.
