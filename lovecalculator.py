print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")
name2 = input("What is your crush's name? ")

combined_name = name1 + name2
lower_combined_name = combined_name.lower()
"""
Here we go i am trying comment with three " symboles
"""
t = lower_combined_name.count("t")
r = lower_combined_name.count("r")
u = lower_combined_name.count("u")
e = lower_combined_name.count("e")
first_digit = t + r + u + e

l = lower_combined_name.count("l")
o = lower_combined_name.count("o")
v = lower_combined_name.count("v")
e = lower_combined_name.count("e")
second_digit = l + o + v + e
#score
score = int(str(first_digit) + str(second_digit))

if score < 10 or score > 90:
    print(f"Your score is {score}. Congratulations! You are already together like Coke. I propose you to be engaged!")
elif 40 < score < 50:
    print(f"Your score is {score}. You are alright together; it's fine.")
else:
    print(f"Your score is {score}. I'm sorry to tell you that you can't match each other!")
