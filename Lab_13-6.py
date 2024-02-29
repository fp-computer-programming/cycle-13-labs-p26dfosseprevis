almamater = open("alma_mater.txt","r") #opens file

while True: #this is literaly just the code from schoology
    line = almamater.readline() #reads the next line from the file
    if len(line) == 0: #will only print a line if it exists
        break
    print (line,end="") # prints a line from the file and then sets line to "" for logic
    
    
almamater.close()  #closes file after im done with it