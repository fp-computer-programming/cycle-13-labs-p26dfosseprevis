def grade_checker(dic):
    """Takes a dic of assinment names and grades and prints the grade and assinment for each"""
    for (k,v) in dic.items():
        print(f"I got a {v} on {k}")
def disemvowel(string_):
    """takes a string and removes all vowels"""
    i = 0
    vowel = ["a","e","i","o","u","A","E","I","O","U",]
    string = list(string_)
    while i < len(string_):
        string[i] = "" if string[i] in vowel else string[i]
        i += 1
    return "".join(string)
def count_sheep(n):
    "takes a number n and returns a string counting n sheep"
    o = ""
    i = 0
    while i < n:
        o += f"{i+1} sheep..."
        i += 1
    return o

def sum_array(a):
    """retuens the sum of a array"""
    i = 0
    o = 0
    while i < len(a):
        o += a[i]
        i += 1
    return o    

def add_nums(list):
    """asks the user for numbers to add until the users dosen't give a real number"""
    new_list = list
    inv = input("give me a number:")
    try:
        inv = int(inv) # will only run calculation if this dosen't give a error
        new_list = []
        for num in list:
            new_list.append(num * inv)
    except:
        print("ERROR: please give me a actual number and not text")    
    finally:
        print(f"passed list:{new_list}; User input:{inv}") #print

def score_shananagans(scores):
    """takes a list scores and returns that list after a lot of score_shananagans is done to it"""
    print(f"the max score is:{max(scores)}")
    print(f"the min score is:{min(scores)}")
    print(f"the avg score is:{(sum(scores))/len(scores)}")
    better = 0
    for score in scores: #counts student who got over a 90
        better += 1 if score > 90 else 0
    print(f"{better} students got over a 90")    #displays how many students got over a 90
    print("A kid got a 85" if 85 in scores else "noone got a 85") #checks if scores has the number 85
    scores2 = scores #makes new list with name scores2 that is exactly the same as scores
    scores2.sort() #sorts list in assending order
    scores2.reverse() #reverces list so that it is in decending order
    scores2.pop() #removes last score in list 
    return scores2 #prints list 

def validate_username(name):
    """checks if a username is valid under odd requirements"""
    try:
        if len(name) < 6 or len(name) > 12: #checks name length
            return False
        elif not(name[0].isalpha()): #makes shure first letter in name is letter
            return False
        elif not(name.isalnum()):
            return False
        elif not(name[len(name) - 1] == "!" or name[len(name) - 1] == "3" and name[len(name) - 2] == "2" and name[len(name) - 3] == "1"):
            #yea i know its kinda lond but that line was the best idea I had to check the last 3 characters in a string
            return False
        else:
            return True        
    except:
        print("Bro thats not even a string")
        return False 

def double_stuff(list):
    """takes a list and doubles everything inside"""
    for i,v in enumerate(list):
        list[i] = (v + v)  
    return list