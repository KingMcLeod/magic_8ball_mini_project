import random

# random fortune selection
random_number = random.randint(1, 9)
# print("random number picked: ", str(random_number))  # optional debug

name = input("Enter your name: ")
question = input("Enter your question: ")
answer = ""

# map numbers to answers
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

# output formatting with optional name/question handling
if question == "":
  print("Question: Will I win the lottery?")
  print("Magic 8-Ball's answer: " + answer)
elif name == "":
  print("Question: " + question)
  print("Magic 8-Ball's answer: " + answer)
else:
  print(name + " asks: " + question)
  print("Magic 8-Ball's answer: " + answer)
