from sys import argv

scirpt, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of a computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
Yoo live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
