import random


 
  # globals and question  list

score = 0
english = ["bag"," dog","time"," great man","fart","finger","talk","queen","sleep","fish"]
right_answer = ["putea"," kuri ","wā","tangata nui","pāmamao","maihao","korero","kuini","moe","ika"]
option_1 = ["tekau","iwa"," harikoa","  Pineamine"," whawhai","ika","rangatira","kia ora","tumuaki","mapi"]
option_2 = ["kingi","pepa","aporo","panana","riri","taniwha","tōkena","tuara","tu",
 "taringa"]


#define a function to generate a question
def generate_question(english, right_answer, option_1, option_2 ):
  global score
  print ("what is the correct word for", english, "in maori")
  # genrate a random number to determent the sequence of questions
  random_sequence = random.randint(0,2)
#seperate print statements for readabilty
  if (random_sequence == 0):
    print ("A", option_1)
    print ("B", option_2)
    print ("C", right_answer)
    answer = input (). lower()
    if answer == "c":
      score += 1
    else:
      print ("incorrect")
  elif (random_sequence == 1):
    print ("A", option_1)
    print ("B", right_answer)
    print ("C", option_2)
    answer = input (). lower()
    if answer == "b":
      score += 1
    else:
      print ("incorrect")


  elif (random_sequence == 2):
    print ("A", right_answer)
    print ("B", option_2)
    print ("C", option_1)
    answer = input (). lower()
    if answer == "a":
      score += 1
    else:
      print ("incorrect")
      
  print("current score is :"+ str(score))
#genrate 3 questions pulling possible answer
for i in range(0,10):
 generate_question(english[i],right_answer[i],option_1[i],option_2[i])

if score>7:
  print("look at this nice calming waves video to listen to as a reward https://www.youtube.com/watch?v=V-_O7nl0Ii0&list=PL3KnTfyhrIlcudeMemKd6rZFGDWyK23vx&index=4") 

print(score)




