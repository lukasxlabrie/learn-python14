#imports to add variable to script. stores var for later use. AKA Modules
from sys import argv

#defines prompt as > and tells python to take user_name from the user when asking terminal to run python
scirpt, user_name = argv
prompt = '> '

#multple f strings, will prompt for "likes"
print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

#f string and prompts for input "likes"
print(f"Where do you live {user_name}?")
lives = input(prompt)

#asks user to enter type of CPU
print("What kind of a computer do you have?")
computer = input(prompt)

#final f string. combines all user inputs into one print. """ allows for each line to print as typed.
print(f"""
Alright, so you said {likes} about liking me.
Yoo live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
