almamater = open("alma_mater.txt","r")
list = almamater.readlines()
almamater.close()

list.reverse()
list[0] += "\n" #for some reson one of the lines doesnt have a \n so i had to add it
for verce in list:
    print(verce)
