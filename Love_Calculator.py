# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
n1 = name1.lower()
n2 = name2.lower()

n3 = (n1.count ('t') + n1.count('r') + n1.count('u') + n1.count('e'))
n4 = (n2.count ('t') + n2.count('r') + n2.count('u') + n2.count('e'))
n5 = (n1.count ('l') + n1.count('o') + n1.count('v') + n1.count('e'))
n6 = (n2.count ('l') + n2.count('o') + n2.count('v') + n2.count('e'))

n7 = n3+n4
n8 = n5+n6

score = int (str(n7)+ str (n8))

if score < 10 or score > 90:
    print (f"Your score is {score}, you go together like coke and mentos.") 

elif score >= 40 and score <=50:
    print (f"Your score is {score}, you are alright together.")

else:
    print (f"Your score is {score}.")