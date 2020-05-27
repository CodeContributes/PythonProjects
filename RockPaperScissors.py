import math
import os
import random
import re
import sys

while True:
  d =["rock", "paper", "scissors"]
  de = random.choice(d)

  choice = input("Do you choose rock, paper, or scissors? ")

  if de == choice :
    print("You and the computer have the same answer! Try again.")
  elif de == "rock" and choice == "paper":
    print("The computer chose rock. You win!")
  elif de == "rock" and choice == "scissors":
    print("The computer chose rock. You lose!")
  elif de == "paper" and choice == "scissors":
    print("The computer chose paper. You win! ")
  elif de == "paper" and choice == "rock":
    print("The computer chose paper. You lose!")
  elif de == "scissors" and choice == "rock":
    print("The computer chose scissors. You win!")
  elif de == "scissors" and choice == "paper":
    print("The computer chose scissors. You lose!")
  else:
    print("That is not a valid response. Try again.")
    
  print("Do you want to restart ? Yes or No")
  response = input()
  if not response == "Yes":
    break
