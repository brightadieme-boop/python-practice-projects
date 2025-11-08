print("Welcome to the python Quiz Game!\n")
score = 0

answer1 = input("1. What is the capital of france? ").lower()
if answer1 == "paris":
    print("Correct")
    score += 1
else:
    print("Incorrect. The answer is Paris. ")

answer2 = input("2. what is 5 + 7? ")
if answer2 == "12":
    print("Correct!")
    score += 1
else:
    print("Nope! it's 12.")

answer3 = input("3. What keyword is used to define function in Python? ").lower()    
if answer3 == "def":
    print("Correct!")
    score += 1
else:
    print("Incorrect. The answer is 'def'.")

while True:
   answer4 = input("4.What continent is Nigeria located? ").lower()
   if answer4 == "africa":
    print("That's right!")
   else:
    print("Sorry! that's wrong")
   again = input("Try again? (yes/no) ")
   if again.lower() != "yes":
    break
  

  
print(f"\n You got {score} out of 4 correct!")
if score == 4:
     print("perfect score! You're on fire!")
elif score == 3:
 print("Good job! keep going.")
else:
     print("keep practicing - you're learning!")   
                     
                   



