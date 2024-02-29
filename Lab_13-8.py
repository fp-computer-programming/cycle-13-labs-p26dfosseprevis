from datetime import datetime #imports todays date for assinment

file = open("my_file.txt","w") #creates / overwrites a new file
file.write("dfp " + str(datetime.now().date()) + "\n") #adds my initals and todats date to the file
file.write("Hello World!\n") #adds hello world to file then adds a line brake 
file.write("playing games") 

file.close #closes file after im done with it