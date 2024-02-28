almamater = open("alma_mater.txt","r")
list = almamater.readlines()
almamater.close()

list.reverse()
list[0] += "\n"
for verce in list:
    print(verce)
