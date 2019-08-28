import random

#Players

pyplayer = random.randrange(10,100)
userplayer = input("Rock, Paper or Scissors? ")
pyplay = None
userplayer = userplayer.lower()

#Value of py-play

if pyplayer %2 ==0:
  pyplay= "rock"
elif pyplayer %3==0:
  pyplay = "paper"
else:
  pyplay = "scissors"

#Game

if pyplay == userplayer:
  print("Draw!")
elif pyplay == "rock" and userplayer == "paper":
  if pyplay == "rock" and userplayer == "scissors":
     print("Python wins. Rock smashes scissors!")
  print("You win. Paper covers rock!")
elif pyplay == "paper" and userplayer == "scissors":
  if pyplay == "paper" and userplayer == "rock":
     print("Python wins. Paper covers rock")
  print("You win. Scissors cuts paper!")
elif pyplay == "scissors" and userplayer == "paper":
  if pyplay == "scissors" and userplayer == "rock":
     print("You win. Rock smashes scissors!")
  print("Python wins. Scissors cuts paper!")
else	:
  print("Enter game again 	")