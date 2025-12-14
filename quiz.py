print("\n 🎉 welome our quiz session 🔆")
score = 0

print("(1).  what is the full form of the Html ?\n ")
print("(a). Hyper Text Make Language")
print("(b).Hyper Text Markup Language")
print("(C).Home Tool Markup Language")
print("(d).Hyperlinks and Text Management Language")
answer = input("your choose the your answer(A/B/C/D)").strip().lower()

if answer == "b":
   print("your  answer is   correct ")
   score +=1

else:
   print("your answer is w wrong:❌")  

    

print("(2).Which tag is used to create a hyperlink in HTML?  \n")
print("(a).<link>")
print("(b).<a>")
print("(c).<href>")
print("(d).<hrf>")

answer = input ("your choose answer is (A/B/C/D)").strip().lower()

if answer == "b":
    print("☑️your answer is correct☑️")
    score += 1
else:
    print("❌your  answer is wrong  the correct answer is ☑️ B")

print("(3).Which tag is used for the largest heading?")   
print("(a).<h6)") 
print("(b).<h5>") 
print("(c).<h1>") 
print("(d).<h3>") 

answer = input ("your choose  answer is (A/B/C/D)").strip().lower()
if   answer =="c":
        print(" ☑️ your answer is correct ☑️")
        score +=1
else: 
    print(" ❌your answer is wrong the correct answer is (c)")     


print("(4).The correct file extension for HTML file is:?")   
print("(a) .doc") 
print("(b) .txt") 
print("(c) .Html") 
print("(d) .js") 

answer = input ("your choose  answer is (A/B/C/D)").strip().lower()
if   answer =="c":
        print("your answer is correct ☑️")
        score +=1
else: 
    print("  ❌ your answer is wrong the correct answer is (c).")   

print(f"your final score is :{score}/4  ")
if score == 4 : 
    print("excellent:🎉")
elif  score == 3:
        print("your are good :")
elif score == 2 :
        print(" ☠️ you  are weeek  try again ")
else:
        print("you are fail please try again ! ")  

  

      


