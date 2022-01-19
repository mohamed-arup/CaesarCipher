import os
import sys
from logo import encode_logo, decode_logo
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if 'windows' in sys.platform:
  def clear():
    os.system('cls')
else:
  def clear():
    os.system('clear')
    
upper_alpha = []

for item in alpha:
  upper_alpha += item.upper()

question = input("Type 1 for encode, type 2 for decode: ")

while question != "1" and question !="2":
  print("\nInvalid response\n")
  question = input("Make sure you type 1 for encode, type 2 for decode: ")

clear()

if question == "1":
  print(encode_logo) 
elif question == "2":
  print(decode_logo)

text = input("Insert text:\n")
shift = int(input("What is the shift:\n")) % 26

def encode():
  shifted = ''
  for char in text:
    if str.isupper(char) == True:
      shifter = (upper_alpha.index(char) + shift)
      if shifter >= 26:
        #print(f"The shift was HIGH at {shifter}")
        shifter = (shifter % 26)
        #print(f"The NEW shift is now {shifter}")
      #print(alpha.index(char))
        shifted += upper_alpha[shifter]
      else:
        shifted += upper_alpha[shifter]
    elif char in alpha :
      shifter = (alpha.index(char) + shift)
      if shifter >= 26:
        #print(f"The shift was HIGH at {shifter}")
        shifter = (shifter % 26)
        #print(f"The NEW shift is now {shifter}")
        shifted += alpha[shifter]
      #print(alpha.index(char))
      else:
        shifted += alpha[shifter]
    else:
      shifted += char
  print(shifted)

def decode():
  shifted = ''
  for char in text:
    if str.isupper(char) == True:
      shifter = ((upper_alpha.index(char)) + (26 - shift))
      if shifter >= 26:
        #print(f"The shift was HIGH at {shifter}")
        shifter = (shifter % 26)
        #print(f"The NEW shift is now {shifter}")
      #print(alpha.index(char))
        shifted += upper_alpha[shifter]
      else:
        shifted += upper_alpha[shifter]
    elif char in alpha:
      shifter = (alpha.index(char) + shift)
      if shifter >= 26:
        #print(f"The shift was HIGH at {shifter}")
        shifter = (shifter % 26)
        #print(f"The NEW shift is now {shifter}")
      #print(alpha.index(char))
        shifted += alpha[alpha.index(char) - shift]
      else:
        shifted += alpha[alpha.index(char) - shift]
    else:
      shifted += char
  print(shifted)

if question == "1":
  encode()
elif question == "2":
  decode()
