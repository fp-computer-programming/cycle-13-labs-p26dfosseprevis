grades = {"lab 1-1":100,"lab 2-2":100,"lab 2-3":100,"lab 2-4":100,"lab 2-5":100,"lab 2-6":100,"lab 2-7":100,"lab 2-8":100,"lab 2-9":100
          ,"lab 3-1":100,"lab 3-2":100,"lab 3-3":100,"lab 3-4":100,"lab 3-5":100,"lab 3-6":100} #list of assinments and grades from Q1

print((grades.values()))

for (k,v) in grades.items():
    print(f"I got a {v} on {k}") #goes into every grade i got and prints each of them followed by the assinment name
for (k,v) in grades.items():
    if v >= 70:
        print(f"I got a {v} on {k} thats over 70") #goes into every grade i got and prints each of them followed by the assinment name if the grade is >70
for (k,v) in grades.items():
    if v >= 50:
        print(f"I got a {v} on {k} thats over 50")#goes into every grade i got and prints each of them followed by the assinment name if the grade is >50