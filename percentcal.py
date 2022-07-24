
def check80(sname,marks) :
  while marks > 80:
    marks = int(input(f"What is your {sname} Marks? ")) 
  else:
    return marks
    


Engmark = int(input("What is your English Marks? "))
subname = "English" 
Engmark = check80(subname,Engmark)

Scimark = int(input("What is your Science Marks? "))
subname = "Science"
Scimark = check80(subname,Scimark)

Mathmark = int(input("What is your Mathematics Marks? "))
subname = "Mathematics"
Mathmark = check80(subname,Mathmark)

Socmark = int(input("What is your Social Science Marks? "))
subname = "Social Science"
Socmark = check80(subname,Socmark)

Langmark = int(input("What is your II Language Marks? "))
subname = "II Language"
Langmark = check80(subname,Langmark)


def check30(psname,pmarks) :
  while pmarks > 20:
    pmarks = int(input(f"What is your {psname} Marks? ")) 
  else:
    return pmarks
  
  
Opt = input("Have you combined your internals and practical marks? y/n ") 
if Opt == "y":
  Result = (Engmark+Scimark+Mathmark+Socmark+Langmark)/5 
  
elif Opt == "n" :
  PraEng = int(input("What is your English Internal Marks? ")) 
  psubname = "English Internal"
  PraEng = check30(psubname,PraEng)
  
  PraSci = int(input("What is your Science Internal and Practical Marks? ")) 
  psubname = "Science Internal and Practical"
  PraEng = check30(psubname,PraSci)
  
  PraMath = int(input("What is your Mathematics Internal Marks? ")) 
  psubname = "Mathematics Internal"
  PraEng = check30(psubname,PraMath)
  
  PraSoc = int(input("What is your Social Science Internal Marks? "))
  psubname = "Social Science Internal"
  PraEng = check30(psubname,PraSoc) 
  
  PraLang = int(input("What is your II Language Internal Marks? "))
  psubname = "II Language Internal"
  PraEng = check30(psubname,PraLang) 
  
  Result = (Engmark+PraEng+Scimark+PraSci+Mathmark+PraMath+Socmark+PraSoc+Langmark+PraLang)/5 
  
  
else: 
  print("The in put is not valid :(") 
  
print("Calculation...")
print("You Result Percentage is ",Result,"%")
if Result >= 35 :
  print("You Passed!")
  
else: 
  print("Your Failed!")