almamater = open("alma_mater.txt","r")

while True: #this is literaly just the code from schoology
    line = almamater.readline()
    if len(line) == 0:
        break
    print (line,end="")
    
    
almamater.close()