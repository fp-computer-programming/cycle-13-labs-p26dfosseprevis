from datetime import datetime 

file = open("my_file.txt","w")
file.write("dfp " + str(datetime.now().date()) + "\n")
file.write("Hello World!\n")
file.write("playing games")

file.close