almamater = open("alma_mater.txt","r") #reads file
list = almamater.readlines() #reads file and converts it to list
almamater.close() #closes file after im done with it

list.reverse() #reverses list containing file
list[0] += "\n" #for some reson one of the lines doesnt have a \n so i had to add it
for verse in list: #prints every verse in the file line by line
    print(verse)
