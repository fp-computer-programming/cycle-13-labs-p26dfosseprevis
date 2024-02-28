almamater = open("alma_mater.txt","r")

while True:
    line = almamater.readline()
    if len(line) == 0:
        break
    print (line,end="")
    
    
almamater.close()